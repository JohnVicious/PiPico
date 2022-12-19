import time

class DHTTemp:

    def __init__(self,dht_sensor,digital_display,board_led,exit_btn):
        self.dht_sensor = dht_sensor
        self.digital_display = digital_display
        self.board_led = board_led
        self.exit_btn = exit_btn

    def startProject(self):        
        self.digital_display.show('load')
        time.sleep_ms(750)

        while True:
            if self.exit_btn.triggered():
                break

            self.board_led.toggle()
            
            T,H = self.dht_sensor.read()

            if T is None:
                print(" sensor error")
            else:
                Ctemp = T
                Ftemp = int(str((Ctemp * 1.8) + 32)[:2])
                self.digital_display.temperature(Ftemp)
