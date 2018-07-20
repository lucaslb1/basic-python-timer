import time
import threading


class Stopwatch(threading.Thread):

    def __init__(self, holder, command_queue):
        threading.Thread.__init__(self)
        self.holder = holder
        self.command_queue = command_queue

    def run(self):
        start_time = time.time()
        time_diff = 0

        is_running = False

        # Loop that constantly runs
        while True:
            if not self.command_queue.empty():
                command = self.command_queue.get()
                if command == "stop" and is_running:
                    is_running = False
                    time_diff = time.time() - start_time
                elif command == "start" and not is_running:
                    is_running = True
                    start_time = time.time() - time_diff
                elif command == "reset":
                    time_diff = 0
                    self.holder.held_time = 0
                    is_running = False
                elif command == "quit":
                    break

            if is_running:
                self.holder.held_time = time.time()-start_time

            time.sleep(.05)
