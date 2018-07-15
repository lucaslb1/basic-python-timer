from tkinter import *
from queue import Queue
from Timer import Timer


# Creates a window which runs a single timer inside of it
# Queue is used to communicate with Timer thread
class TimerWindow:

    def __init__(self):
        # Initializes state as not running
        self.is_running = False

        # Queue used to communicate between timer and GUI threads
        self.time_queue = Queue()

        # Creating the window
        self.window = Tk()
        self.window.geometry("150x100")
        self.window.title("Countdown Timer")

        # The StringVar holds the Entry's text
        self.user_time_field_string = StringVar()

        # The field which the user enters their time into
        self.user_time_field = Entry(self.window, width=10, textvariable=self.user_time_field_string)
        self.user_time_field.pack()

        # Button which starts the timer
        self.start_button = Button(self.window, text="Start", command=self.start_timer)
        self.start_button.pack()

        # Initializes current time as self attribute
        self.current_time = Label(self.window)
        self.current_time.pack()

        self.window.mainloop()

    def start_timer(self):

        # If the text in the text box is an integer
        if self.user_time_field_string.get().isdigit() and not self.is_running:

            # Changes state of TimerWindow
            self.is_running = True

            # Get the input integer
            user_time = int(self.user_time_field_string.get())

            # Create a label that shows the countdown
            self.current_time.configure(text=str(user_time))

            # Create timer object
            t1 = Timer("{} second timer".format(user_time), self.time_queue, user_time)
            t1.start()

            # Simulates mainloop()
            while True:
                self.window.update_idletasks()
                self.window.update()

                # Checks Queue
                if not self.time_queue.empty():
                    time_value = self.time_queue.get()

                    # Displays timer value or
                    if time_value > 0:
                        self.current_time.configure(text=str(time_value))
                    else:
                        self.current_time.configure(text="{} second timer\nfinished".format(user_time))
                        self.is_running = False


if __name__ == "__main__":
    window1 = TimerWindow()
