from timeit import default_timer as timer

class TimeCounter:
    elapsed = 0

    def __init__(self):
        self.elapsed = 0
        self.start = 0
        self.end = 0

    def timeStart(self):
        self.start = timer()

    def timeStop(self):
        self.end = timer()
        self.elapsed = self.end - self.start
        return self.elapsed