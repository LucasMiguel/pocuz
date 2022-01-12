from threading import Thread
import time


class ThreadCountTime(Thread):
    def __init__(self, time):
        Thread.__init__(self)
        self.timeCount = time
        self.runCount = False

    def run(self):
        while True:
            if self.runCount:
                self.timeCount = self.timeCount - 1
                print(self.timeCount)
                self.timeLabel.setText(str(self.timeCount))
                if self.timeCount == 0:
                    self.stop()
                time.sleep(1)

    def play(self):
        self.runCount = True

    def pause(self):
        self.runCount = False

    def parseTimeLabel(self, labelTime):
        self.timeLabel = labelTime
        
