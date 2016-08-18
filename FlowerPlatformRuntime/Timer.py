import time

class TimerEvent :

    timer = None


class Timer :

    onTimer = None

    onTimerComplete = None

    delay = 1000

    repeatCount = 0

    """
    @flowerChildParameter { ref = "autoStart", type = "bool" }
    """
    def __init__(self, autoStart = False):
        self.started = autoStart

    def setup(self) :
        self.currentCount = 0;
        self.lastTimestamp = time.time() * 1000;
        return

    def loop(self) :
        if (not self.started) :
            return

        if (self.repeatCount > 0 and self.currentCount > repeatCount) :
            self.started = False
            return

        currentTime = time.time() * 1000;
        if (currentTime > self.lastTimestamp + self.delay) :
            self.currentCount = self.currentCount + 1;
            
            event = TimerEvent()
            event.timer = self

            if (self.onTimer != None) :
                self.onTimer(event)

            if (self.repeatCount > 0 and self.currentCount == self.repeatCount) :
                if (self.onTimerComplete != None) :
                    self.onTimerComplete(event)
                self.started = False
                
            self.lastTimestamp = currentTime;

    def reset(self) :
        self.started = False
        self.currentCount = 0

    def start(self) : 
        self.lastTimestamp = time.time() * 1000
        self.started = True

    def stop(self) :
        self.started = False
