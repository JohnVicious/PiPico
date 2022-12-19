from machine import Pin, Timer
import time

boardLed = Pin("LED", Pin.OUT)
beep = Pin(1, Pin.OUT)
btn1 = Pin(2, Pin.IN, Pin.PULL_UP)
btn2 = Pin(3, Pin.IN, Pin.PULL_UP)
btn3 = Pin(4, Pin.IN, Pin.PULL_UP)
btn4 = Pin(5, Pin.IN, Pin.PULL_UP)
led1 = Pin(6, Pin.OUT)
led2 = Pin(7, Pin.OUT)    
led3 = Pin(8, Pin.OUT)    
led4 = Pin(9, Pin.OUT)

def btn1Action():
    btn = btn1
    led = led1  
    triggered = 0
    
    if not btn.value():
        boardLed.value(1)
        led.value(1)
        triggered = 1
    else:
        boardLed.value(0)
        led.value(0)
    
    return triggered

def btn2Action():
    btn = btn2
    led = led2    
    triggered = 0
    
    if not btn.value():
        boardLed.value(1)
        led.value(1)
        triggered = 1
    else:
        boardLed.value(0)
        led.value(0)
    
    return triggered

def btn3Action():
    btn = btn3
    led = led3    
    triggered = 0
    
    if not btn.value():
        boardLed.value(1)
        led.value(1)
        triggered = 1
    else:
        boardLed.value(0)
        led.value(0)
    
    return triggered

def btn4Action():
    btn = btn4
    led = led4   
    triggered = 0
    
    if not btn.value():
        boardLed.value(1)
        led.value(1)
        triggered = 1
    else:
        boardLed.value(0)
        led.value(0)
    
    return triggered


# RUNTIME
while True:
    allPressed = 0
    
    allPressed += btn1Action()
    allPressed += btn2Action()
    allPressed += btn3Action()
    allPressed += btn4Action()
    
    if allPressed >= 4:
        beep.value(1)
    else:
        beep.value(0)
