import time

class TransitorTemp:

    def __init__(self,transitor_sensor,digital_display,board_led,exit_btn):
        self.transitor_sensor = transitor_sensor
        self.digital_display = digital_display
        self.board_led = board_led
        self.exit_btn = exit_btn

    def startProject(self):        
        self.digital_display.show('load')
        time.sleep_ms(750)
        self.digital_display.temperature(self.addOn_Temp())

        count = 0
        totalTemp = 0

        while True:
            if self.exit_btn.triggered():
                break

            self.board_led.toggle()
            
            totalTemp += self.addOn_Temp()
            count += 1
            
            if count > 9:
                temp = int(str(totalTemp / count)[:2])
                self.digital_display.temperature(temp)
                count = 0
                totalTemp = 0
            
            time.sleep_ms(100)
    
    def addOn_Temp(self):
        conversion_factor = 3.3/65535 # based of 5v supply and 16 bit value
        
        # Read ADC value of sensor
        temp_voltage_raw = self.transitor_sensor.read_u16()
        
        # Converts ADC value back to voltage
        convert_voltage = temp_voltage_raw*conversion_factor
        
        C_temp = convert_voltage/(10.0 / 1000)
        
        F_temp = (C_temp*9/5) +32
        
        return int(str(F_temp)[:2]) - 6