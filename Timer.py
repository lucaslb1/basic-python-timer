import sys
from tkinter import *
import threading
from queue import Queue
import time


class Timer:

    def __init__(self, name, length):
        self.name = name
        self.length = length

    def __str__(self):
        return "{} for {}".format(self.name, self.length)

    def start(self):
        print("Timer {} for {} seconds is started".format(self.name, self.length))

        for x in range(0, self.length):
            time.sleep(1)

        print("Timer {} for {} seconds is finished".format(self.name, self.length))


def main():
    root = Tk()
    if len(sys.argv) > 2:
        test = Timer(sys.argv[1], int(sys.argv[2]))
        message = Label(root, text=str(test))
        message.pack()

        root.update()
        test.start()
        message = Label(root, text="Finished")
        message.pack()
        while True:
            root.update()

    else:
        message = Label(root, text="Please include the name and duration of the timer in the arguments")
        message.pack()
        while True:
            root.update()


if __name__ == "__main__":
    main()
