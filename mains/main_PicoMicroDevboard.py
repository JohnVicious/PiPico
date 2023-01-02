from machine import Pin, ADC, I2C
from libs.tm1637 import *
from libs.ssd1306 import *
from libs.PicoDHT22 import *
from classes.button import button
from classes.led import led
from classes.buzzer import buzzer
import time

#SETUP - switches, buzzers, leds, displays, sensors, etc...
board_led = led(Pin("LED", Pin.OUT))
i2cdisplay = SSD1306_I2C(128, 64, I2C(0, sda=Pin(0), scl=Pin(1), freq=400000))
i2cdisplay.fill(0)
i2cdisplay.text('Loading!', 0, 0, 1)
i2cdisplay.show()
time.sleep_ms(1000)
i2cdisplay.fill(0)
i2cdisplay.text('TEST', 0, 20, 1)
i2cdisplay.show()

while True:
    board_led.toggle()
    time.sleep_ms(1000)