from tkinter import *
from TimerWindow import TimerWindow
from StopwatchWindow import StopwatchWindow
import time

# This class will allows me to switch between windows, eg a timer, stopwatch, clock
class TimeApp(Tk):

    # Constructor
    def __init__(self):

        # Parent constructor
        Tk.__init__(self)
        self.geometry("150x100")
        self.title("Time App")
        self.resizable(height=False, width=False)

        # Holds status of current window displayed
        self.current_window = "none"

        # Initializes timer_window frame and pass self as the root
        self.timer_window = TimerWindow(self)

        # Initializes stopwatch_window with self as root
        self.stopwatch_window = StopwatchWindow(self)

        # Initializes the menu
        self.top_menu = Frame(self)

        # Buttons used to switch between frames
        self.timer_menu_button = Button(self.top_menu, command=self.activate_timer, text="timer").pack(side=LEFT)
        self.stopwatch_menu_button = Button(self.top_menu, command=self.activate_stopwatch, text="stopwatch").pack(side=LEFT)

        # Packs the menu
        self.top_menu.pack()

        # Packs the desired first window
        self.activate_timer()

        self.master_loop()

    def master_loop(self):
        while True:
            self.update_idletasks()
            self.update()
            if self.current_window == "stopwatch":
                self.stopwatch_window.update_text()
            if self.current_window == "timer":
                self.timer_window.update_text()

    # Switches to the timer frame and makes the previous one invisible
    def activate_timer(self):
        if self.current_window != "timer":
            self.unpack()
            self.stopwatch_window.is_displayed = False

            self.timer_window.pack()
            self.current_window = "timer"
            self.timer_window.is_displayed = True
            print("Switching to timer")

    # Switches to the stopwatch frame and makes the previous one invisible
    def activate_stopwatch(self):
        if self.current_window != "stopwatch":
            self.unpack()
            self.timer_window.is_displayed = False

            self.stopwatch_window.pack()
            self.current_window = "stopwatch"
            self.stopwatch_window.is_displayed = True
            print("Switching to stopwatch")

    # Makes the current frame invisible
    def unpack(self):
        if self.current_window == "timer":
            self.timer_window.pack_forget()
        elif self.current_window == "stopwatch":
            self.stopwatch_window.pack_forget()

    def destroy(self):
        self.stopwatch_window.quit()
        Tk.destroy(self)

if __name__ == "__main__":
    time_app = TimeApp()
