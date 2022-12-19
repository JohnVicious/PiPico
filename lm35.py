from machine import Pin, Timer, ADC
import time

sensor = ADC(26)

def addOn_Temp():
    conversion_factor = 3.3/65535 # based of 5v supply and 16 bit value
    
    # Read ADC value of sensor
    temp_voltage_raw = sensor.read_u16()
    
    # Converts ADC value back to voltage
    convert_voltage = temp_voltage_raw*conversion_factor
    
    C_temp = convert_voltage/(10.0 / 1000)
    
    F_temp = (C_temp*9/5) +32
    
    print("raw voltage: ", temp_voltage_raw, "\t converted voltage: ",convert_voltage, "\t Temperature(C): ",C_temp, "\t Temperature(F): ",F_temp)
   
# RUNTIME
while True:
    addOn_Temp()
    
    time.sleep(3)