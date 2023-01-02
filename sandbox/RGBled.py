from machine import Pin, ADC, I2C, PWM
from libs.tm1637 import *
from libs.ssd1306 import *
from libs.PicoDHT22 import *
from classes.button import button
from classes.led import led
from classes.buzzer import buzzer
import time
import random

#SETUP - switches, buzzers, leds, displays, sensors, etc...
board_led = led(Pin("LED", Pin.OUT))
led_R = PWM(Pin(2))
led_G = PWM(Pin(3))
led_B = PWM(Pin(4))
led_R.freq(2000)
led_G.freq(2000)
led_B.freq(2000)


while True:
    board_led.toggle()

    #R=int(65535)
    #G=int(65535)
    #B=int(65535)
    R=random.randint(0,65535)
    G=random.randint(0,65535)
    B=random.randint(0,65535)

    led_R.duty_u16(R) 
    led_G.duty_u16(G) 
    led_B.duty_u16(B)

    time.sleep_ms(1000)
    