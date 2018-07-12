from tkinter import *
from queue import Queue
from Timer import Timer

class TimerWindow:

    def __init__(self, name, length):
        self.time_queue = Queue()
        self.time_queue.put(length)
        self.name = name
        self.length = length

        window = Tk()
        window.geometry("200x200")
        window.title(name)
        current_time = Label(window, text=str(length))
        current_time.pack()
        t1 = Timer(self.name, self.time_queue, self.length)
        t1.start()
        while True:
            window.update_idletasks()
            window.update()
            if not self.time_queue.empty():
                time_value = self.time_queue.get()
                current_time.configure(text=str(time_value))




window1 = TimerWindow("Test", 10)