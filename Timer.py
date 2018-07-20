import threading
import time
from sys import platform


# Uses a Queue to communicate with the TimerWindow GUI
class Timer (threading.Thread):

    # Constructor
    def __init__(self, holder):
        threading.Thread.__init__(self)
        self.length = holder.held_time
        self.holder = holder

        # Alarm sound file
        self.audio_file = "alarm_sound.wav"

    # Timer starts when thread is started
    def run(self):
        print("{} second timer started".format(self.length))
        start_time = time.time()
        while True:
            if time.time()-start_time < self.length:
                time.sleep(.05)
                self.holder.held_time = self.length - (time.time()-start_time)
            else:
                self.holder.held_time = float(0)
                break
        print("{} second timer finished".format(self.length))
        self.play_audio()

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

