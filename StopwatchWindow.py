from tkinter import *


class StopwatchWindow(Frame):

    def __init__(self, root,  is_displayed=False):

        # Parent class constructor
        Frame.__init__(self, root)
        self.root = root
        self.is_displayed = is_displayed

        self.text_label = Label(self, text="Hello Stopwatch")
        self.text_label.pack()

        if self.is_displayed:
            self.pack()