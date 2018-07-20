# Used to as tool to communicate the current time between threads


class TimeHolder:
    def __init__(self, held_time):
        self.held_time = held_time

