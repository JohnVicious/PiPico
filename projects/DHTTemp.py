import time

class DHTTemp:

    def __init__(self,dht_sensor,digital_display,i2cdisplay,board_led,exit_btn):
        self.dht_sensor = dht_sensor
        self.digital_display = digital_display
        self.i2cdisplay = i2cdisplay
        self.board_led = board_led
        self.exit_btn = exit_btn

    def startProject(self):        
        self.digital_display.show('load')
        self.i2cdisplay.fill(0)
        self.i2cdisplay.text('Loading!', 0, 0, 1)
        self.i2cdisplay.show()
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
                self.updateI2CDisplay(Ftemp,H)

    def updateI2CDisplay(self,temperature,humidity):
        self.i2cdisplay.fill(0)
        self.i2cdisplay.text('Temp: ' + str(temperature) + 'F', 0, 0, 1)
        self.i2cdisplay.text('Humidity: ' + str(humidity) + '%', 0, 10, 1)
        self.i2cdisplay.text('K4 To Exit =>', 0, 50, 1)
        self.i2cdisplay.show()
