import threading
import time
import Tkinter as tk

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

class GUI (tk.Frame):
	
	def __init__(self, master=None)
		tk.Frame.__init__(self, master)
		self.


Timer("test1", 5).start()
Timer("test2", 7).start()
