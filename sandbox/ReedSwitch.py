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
sensor_led = led(Pin(13, Pin.OUT))
reed_sensor = Pin(5, Pin.IN, Pin.PULL_UP)
i2cdisplay = SSD1306_I2C(128, 64, I2C(0, sda=Pin(0), scl=Pin(1), freq=400000))


#Show startup
board_led.off()
i2cdisplay.fill(0)
i2cdisplay.text('Loading!', 0, 0, 1)
i2cdisplay.show()
time.sleep_ms(1000)

while True:

    board_led.toggle()
    sensor_led.toggle()
    i2cdisplay.fill(0)
    i2cdisplay.text('Reed switch: ', 0, 10, 1)

    if reed_sensor.value() == 0:
        i2cdisplay.text('detected!', 0, 30, 1)

    i2cdisplay.show()
    time.sleep_ms(100)