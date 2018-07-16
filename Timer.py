import threading
import time
from tkinter import *
from queue import Queue


# Uses a Queue to communicate with the TimerWindow GUI
class Timer (threading.Thread):

    # Constructor
    def __init__(self, name, time_queue, length, is_running=False):
        threading.Thread.__init__(self)
        self.name = name
        self.time_queue = time_queue
        self.length = length
        self.is_running = is_running

    def __str__(self):
        return "{}".format(self.name)

    # Timer starts when thread is started
    def run(self):
        self.is_running = True
        print("{} started".format(self.name))
        start_time= time.time()
        while True:
            if time.time()-start_time < self.length:
                time.sleep(.1)
                self.time_queue.put(self.length - (time.time()-start_time))
            else:
                break
        print("{} finished".format(self.name))


