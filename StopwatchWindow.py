from tkinter import *
from queue import Queue
from Stopwatch import Stopwatch


class StopwatchWindow(Frame):

    def __init__(self, root,  is_displayed=False):

        # Parent class constructor
        Frame.__init__(self, root)
        self.root = root
        self.is_displayed = is_displayed

        # Buttons used to interact with the the stopwatch
        self.start_button = Button(self, command=self.start, text="start").pack(side=LEFT)
        self.stop_button = Button(self, command=self.stop, text="stop").pack(side=LEFT)
        self.reset_button = Button(self, command=self.reset, text="reset").pack(side=LEFT)

        # Things to do, queue to send commands, label that updates in its mainloop
        self.time_queue = Queue()
        self.command_queue = Queue()

        # Creates and starts the stopwatch thread
        self.stopwatch = Stopwatch(self.time_queue, self.command_queue)
        self.stopwatch.start()

        # Creates label which holds the stopwatch time
        self.time_label = Label(self, text="0.0")
        self.time_label.pack()

        if self.is_displayed:
            self.pack()

    def update_text(self):
        if not self.time_queue.empty():
            time_value = self.time_queue.get()
            self.time_label.configure(text="{0:.1f}".format(time_value))

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