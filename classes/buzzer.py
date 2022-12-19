from machine import Pin
import utime as time

class buzzer:
    
    def __init__(self,dataPin):
        self.dataPin = dataPin
        self.dataPin.init(Pin.OUT)
    
    def beep(self):
        self.dataPin.value(1)
        time.sleep_ms(50)
        self.dataPin.value(0)

