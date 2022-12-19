import tm1637
from machine import Pin, Timer
import time

tm = tm1637.TM1637(clk=Pin(1), dio=Pin(0))

# RUNTIME
tm.temperature(1)