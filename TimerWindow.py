from tkinter import *
from queue import Queue
from Timer import Timer


class TimerWindow:

    def __init__(self):

        # Queue used to communicate between timer and GUI threads
        self.time_queue = Queue()

        # Creating the window
        self.window = Tk()
        self.window.geometry("200x200")
        self.window.title("Countdown Timer")

        # The StringVar holds the Entry's text
        self.user_time_field_string = StringVar()

        # The field which the user enters their time into
        self.user_time_field = Entry(self.window, width=10, textvariable=self.user_time_field_string)
        self.user_time_field.pack()

        # Button which starts the timer
        self.start_button = Button(self.window, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.window.mainloop()

    def start_timer(self):
        if self.user_time_field_string.get().isdigit():
            user_time = int(self.user_time_field_string.get())

            self.time_queue.put(user_time)
            current_time = Label(self.window, text=str(user_time))
            current_time.pack()
            t1 = Timer("temp", self.time_queue, user_time)
            t1.start()

            while True:
                self.window.update_idletasks()
                self.window.update()
                if not self.time_queue.empty():
                    time_value = self.time_queue.get()
                    if time_value > 0:
                        current_time.configure(text=str(time_value))
                    else:
                        current_time.configure(text="Timer for {} seconds finished".format(user_time))


window1 = TimerWindow()