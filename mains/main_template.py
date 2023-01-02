from machine import Pin, ADC, I2C
from libs.tm1637 import *
from libs.ssd1306 import *
from libs.PicoDHT22 import *
from classes.button import button
from classes.led import led
from classes.buzzer import buzzer

#SETUP - switches, buzzers, leds, displays, sensors, etc...
board_led = led(Pin("LED", Pin.OUT))

while True:
    board_led.toggle()