import threading
import time
from tkinter import *
from queue import Queue


# Uses a Queue to communicate with the TimerWindow GUI
#
class Timer (threading.Thread):

    def __init__(self, name, time_queue, length):
        threading.Thread.__init__(self)
        self.name = name
        self.time_queue = time_queue
        self.length = length

    def __str__(self):
        return "timer name: {}".format(self.name)

    def run(self):
        print("Timer {} is started".format(self.name))
        for x in range(self.length, -1, -1):
            print(x)
            self.time_queue.put(x)
            time.sleep(1)


        print("Timer {} is finished".format(self.name))


