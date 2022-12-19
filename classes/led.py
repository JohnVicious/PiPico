from machine import Pin

class led:
    
    def __init__(self,dataPin):
        self.dataPin = dataPin
        self.dataPin.init(Pin.OUT)
    
    def on(self):
        self.dataPin.value(1)

    def off(self):
        self.dataPin.value(0)

    def toggle(self):
        self.dataPin.toggle()
