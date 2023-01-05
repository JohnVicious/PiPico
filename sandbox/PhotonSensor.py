from machine import Pin, ADC, I2C
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
i2cdisplay = SSD1306_I2C(128, 64, I2C(0, sda=Pin(0), scl=Pin(1), freq=400000))
photo_sensor = ADC(26)


#Show startup
board_led.off()
i2cdisplay.fill(0)
i2cdisplay.text('Loading!', 0, 0, 1)
i2cdisplay.show()
time.sleep_ms(1000)

while True:
    photons = photo_sensor.read_u16()

    if photons > 10000:
        lightStatus = 'on'
        board_led.on()
    else:
        lightStatus = 'off'
        board_led.off()


    i2cdisplay.fill(0)
    i2cdisplay.text('Light is ' + str(lightStatus), 0, 30, 1)
    i2cdisplay.show()

    time.sleep_ms(1000)
    