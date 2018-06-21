import threading
import time
from tkinter import *

class Timer (threading.Thread):

    def __init__(self, name, length):
        threading.Thread.__init__(self)
        self.name = name
        self.length = length

        
    def __str__(self):
        return "{} for {}".format(self.name, self.length)

    def run(self):
        print("Timer {} for {} seconds is started".format(self.name, self.length))

        for x in range(0, self.length):
            time.sleep(1)

        print("Timer {} for {} seconds is finished".format(self.name, self.length))



t1 = Timer("test1", 10)
t2 = Timer("test2", 5)
t1.start()
t2.start()
