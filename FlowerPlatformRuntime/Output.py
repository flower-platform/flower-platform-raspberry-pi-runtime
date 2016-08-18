from ValueChangedEvent import ValueChangedEvent
import RPi.GPIO as GPIO

class Output:

    contributesToState = False

    onValueChanged = None

    """
    @flowerChildParameter { ref = "pin", type = "int" }
    @flowerChildParameter { ref = "isPwm", type = "bool" }
    """
    def __init__(self, pin, isPwm = False):
        self.pin = pin
        self.isPwm = isPwm
        self.initialValue = GPIO.LOW
        self.pwm = None

    def setup(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.pin, GPIO.OUT)
      GPIO.output(self.pin, self.initialValue)
      self.lastValue = self.initialValue

    def setValue(self, value):
      if self.isPwm:
          if self.pwm is None:
              self.pwm = GPIO.PWM(self.pin, 1000)
              self.pwm.start(value)
          else:
              self.pwm.ChangeDutyCycle(value)
      else:
          GPIO.output(self.pin, value)
    
      if self.onValueChanged is not None:
          event = ValueChangedEvent()
          event.previousValue = lastValue
          event.currentValue = value
          self.onValueChanged(event)

      self.lastValue = value

    def getValue(self):
      return self.lastValue

    def toggleHighLow(self):
      if self.lastValue == GPIO.HIGH:
          self.setValue(GPIO.LOW)
      else:
          self.setValue(GPIO.HIGH)
        
    def getStateAsJson(self, instanceName):
      return '"{}":{}'.format(instanceName, self.lastValue);

    def loop(self) :
      return

    def stop(self) :
      return
