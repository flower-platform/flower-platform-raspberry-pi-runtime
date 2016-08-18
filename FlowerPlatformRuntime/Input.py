from ValueChangedEvent import ValueChangedEvent
import RPi.GPIO as GPIO
import time

"""
@component
"""
class Input :

    contributesToState = False

    onValueChanged = None

    pollInterval = 50

    """
    @flowerChildParameter { ref = "pin", type = "int" }
    @flowerChildParameter { ref = "internalPullUp", type = "bool" }
    """
    def __init__(self, pin, internalPullUp = True):
        self.pin = pin
        self.internalPullUp = internalPullUp
        self.lastTime = 0
        self.lastValue = GPIO.LOW
    
    def setup(self) :
      GPIO.setmode(GPIO.BCM)
      if self.internalPullUp :
          GPIO.setup(self.pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
          self.lastValue = GPIO.HIGH
      else :
          GPIO.setup(self.pin, GPIO.IN)
          self.lastValue = GPIO.LOW

    def loop(self) :
      value = GPIO.input(self.pin)

      if value == self.lastValue :
          return
    
      if time.time() * 1000 - self.lastTime < self.pollInterval : 
          return
    
      if self.onValueChanged is not None :
          event = ValueChangedEvent
          event.previousValue = self.lastValue
          event.currentValue = value
          self.onValueChanged(event)
    
      self.lastValue = value
      self.lastTime = time.time() * 1000

    def stop(self) :
      return

    def getStateAsJson(self, instanceName) :
      return '"{}":{}'.format(instanceName, self.lastValue);
