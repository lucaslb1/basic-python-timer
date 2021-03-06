from tkinter import *
from queue import Queue
from Timer import Timer
from TimeHolder import TimeHolder


# Creates a window which runs a single timer inside of it
# Queue is used to communicate with Timer thread
class TimerWindow(Frame):

    def __init__(self, root):

        # Parent class constructor
        Frame.__init__(self, root)
        self.root = root

        # Initializes state as not running
        self.is_running = False

        # Queue used to communicate between timer and GUI threads
        self.time_queue = Queue()

        # The StringVar holds the Entry's text
        self.user_time_field_string = StringVar()

        # Frame holding Entry and Button
        self.top_frame = Frame(self)
        self.top_frame.pack(side=TOP, fill=X)

        # The field which the user enters their time into
        self.user_time_field = Entry(self.top_frame, width=10, textvariable=self.user_time_field_string)
        self.user_time_field.pack(side=LEFT)

        # Button which starts the timer
        self.start_button = Button(self.top_frame, text="Start", command=self.start_timer)
        self.start_button.pack(side=LEFT)

        # Creates frame holding countdown so that it may be centered
        self.bottom_frame = Frame(self, width=150)
        self.bottom_frame.pack(side=TOP, fill=X)

        # Initializes current time as self attribute
        self.current_time = Label(self.bottom_frame)
        self.current_time.pack()

        # Timer holder which interacts with current timer
        self.holder = TimeHolder(float(0))

        # Used so update text doesn't display Timer Finished before a timer has gone off
        self.completed_first = False

    # Called in TimeApp's master_loop to update the text on the TimerWindow
    def update_text(self):
        if not self.completed_first:
            pass
        elif self.holder.held_time == 0:
            self.current_time.configure(text="Timer Finished")
        else:
            self.current_time.configure(text="{0:.1f}".format(self.holder.held_time))

    def start_timer(self):

        # If the text in the text box is an integer
        if self.user_time_field_string.get().isdigit() and not self.is_running:

            # Changes state of TimerWindow
            self.is_running = True

            # Get the input integer
            user_time = float(self.user_time_field_string.get())

            # Create a label that shows the countdown
            self.current_time.configure(text=str(user_time))

            # Set holder to hold the correct time
            self.holder.held_time = user_time

            # Create timer object
            t1 = Timer(self.holder)
            t1.start()

            self.completed_first = True
            self.is_running = False


if __name__ == "__main__":
    window1 = TimerWindow()
