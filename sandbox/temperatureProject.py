import tm1637
from machine import Pin, Timer, ADC
import time

sensor = ADC(26)
tm = tm1637.TM1637(clk=Pin(17), dio=Pin(16))

def addOn_Temp():
    conversion_factor = 3.3/65535 # based of 5v supply and 16 bit value
    
    # Read ADC value of sensor
    temp_voltage_raw = sensor.read_u16()
    
    # Converts ADC value back to voltage
    convert_voltage = temp_voltage_raw*conversion_factor
    
    C_temp = convert_voltage/(10.0 / 1000)
    
    F_temp = (C_temp*9/5) +32
    
    return int(str(F_temp)[:2]) - 6
   
count = 0
totalTemp = 0
# RUNTIME
while True:
    totalTemp += addOn_Temp()
    count += 1
    
    if count > 4:
        temp = int(str(totalTemp / count)[:2])
        tm.temperature(temp)
        count = 0
        totalTemp = 0
        print("update")
    
    time.sleep(1)
    


