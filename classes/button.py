from machine import Pin

class button:
    
    def __init__(self,dataPin):
        self.dataPin = dataPin
        self.dataPin.init(Pin.IN, Pin.PULL_UP)
    
    def triggered(self):
        return not self.dataPin.value()
