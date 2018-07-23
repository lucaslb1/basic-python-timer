from tkinter import *
from queue import Queue
from Stopwatch import Stopwatch
from TimeHolder import TimeHolder

class StopwatchWindow(Frame):

    def __init__(self, root,  is_displayed=False):

        # Parent class constructor
        Frame.__init__(self, root)
        self.root = root
        self.is_displayed = is_displayed

        # A frame that holds the buttons
        self.button_frame = Frame(self)
        self.button_frame.pack(side=TOP, fill=X)

        # Buttons used to interact with the the stopwatch
        self.start_button = Button(self.button_frame, command=self.start, text="start").pack(side=LEFT)
        self.stop_button = Button(self.button_frame, command=self.stop, text="stop").pack(side=LEFT)
        self.reset_button = Button(self.button_frame, command=self.reset, text="reset").pack(side=LEFT)

        # Things to do, queue to send commands, label that updates in its mainloop
        self.command_queue = Queue()

        # Creates holder to interact with stopwatch thread with
        self.holder = TimeHolder(float(0))

        # Creates and starts the stopwatch thread
        self.stopwatch = Stopwatch(self.holder, self.command_queue)
        self.stopwatch.start()

        # Creates label which holds the stopwatch time
        self.time_label = Label(self, text="0.0")
        self.time_label.pack()

        if self.is_displayed:
            self.pack()

    def update_text(self):
        # If not self.time_queue.empty():
        self.time_label.configure(text="{0:.1f}".format(self.holder.held_time))

    def start(self):
        self.command_queue.put("start")

    def stop(self):
        self.command_queue.put("stop")

    def reset(self):
        self.command_queue.put("reset")
        self.time_label.configure(text="0.0")

    # so the stopwatch thread stops
    def quit(self):
        self.command_queue.put("quit")