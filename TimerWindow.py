from tkinter import *
from queue import Queue
from Timer import Timer
from sys import platform


# Creates a window which runs a single timer inside of it
# Queue is used to communicate with Timer thread
class TimerWindow(Frame):

    def __init__(self, root, is_displayed = False):

        # Parent class constructor
        Frame.__init__(self, root)
        self.root = root

        # is displayed option
        self.is_displayed = is_displayed

        # Initializes state as not running
        self.is_running = False

        # Alarm sound file
        self.audio_file = "alarm_sound.wav"

        # Queue used to communicate between timer and GUI threads
        self.time_queue = Queue()

        # The StringVar holds the Entry's text
        self.user_time_field_string = StringVar()

        # Frame holding Entry and Button
        self.top_frame = Frame(self)
        self.top_frame.pack(side=TOP, fill=X)

        # The field which the user enters their time into
        self.user_time_field = Entry(self.top_frame, width=10, textvariable=self.user_time_field_string)
        self.user_time_field.pack(side=LEFT)

        # Button which starts the timer
        self.start_button = Button(self.top_frame, text="Start", command=self.start_timer)
        self.start_button.pack(side=LEFT)

        # Creates frame holding countdown so that it may be centered
        self.bottom_frame = Frame(self, width=150)
        self.bottom_frame.pack(side=TOP, fill=X)

        # Initializes current time as self attribute
        self.current_time = Label(self.bottom_frame)
        self.current_time.pack()

        if is_displayed:
            # Packs self into TimeApp root if it should be
            self.pack()

    def start_timer(self):

        # If the text in the text box is an integer
        if self.user_time_field_string.get().isdigit() and not self.is_running:

            # Changes state of TimerWindow
            self.is_running = True

            # Get the input integer
            user_time = float(self.user_time_field_string.get())

            # Create a label that shows the countdown
            self.current_time.configure(text=str(user_time))

            # Create timer object
            t1 = Timer("{} second timer".format(user_time), self.time_queue, user_time)
            t1.start()

            # Simulates mainloop()
            while True:
                self.update_idletasks()
                self.update()

                # Checks Queue
                if not self.time_queue.empty():
                    time_value = self.time_queue.get()

                    # Displays timer value or finished message
                    if time_value > 0:
                        self.current_time.configure(text="{0:.1f}".format(time_value))

                    # Updates text then plays audio file
                    else:
                        self.current_time.configure(text="{} second timer\nfinished".format(user_time))
                        self.update_idletasks()
                        self.update()

                        self.play_audio()
                        self.is_running = False
                        break

    # Plays audio file dependent on os
    def play_audio(self):

        # Uses different methods to play sound depending on system
        if platform == "darwin":
            # OSX
            import subprocess
            return_code = subprocess.call(["afplay", self.audio_file])
            print("Audio return code: {}".format(return_code))
        elif platform == "win32":
            # Windows
            import winsound
            winsound.playsound(self.audio_file, winsound.SND_FILENAME)


if __name__ == "__main__":
    window1 = TimerWindow()
