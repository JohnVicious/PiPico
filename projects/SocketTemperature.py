import time
import network
import socket
from projects.networkcredentials import net_cred

class SocketTemperature:

    def __init__(self,dht_sensor,digital_display,i2cdisplay,board_led,exit_btn):
        self.dht_sensor = dht_sensor
        self.digital_display = digital_display
        self.i2cdisplay = i2cdisplay
        self.board_led = board_led
        self.exit_btn = exit_btn
        self.ip_address = 0

    def startProject(self):        
        self.digital_display.show('load')
        self.i2cdisplay.fill(0)
        self.i2cdisplay.text('Loading!', 0, 0, 1)
        self.i2cdisplay.show()
        time.sleep_ms(750)
        
        self.networkConnection()
        socket_connection = self.socketConnection()
        Ftemp = 'loading'
        while True:         

            T,H = self.dht_sensor.read()
            if T is None:
                print(" sensor error")
            else:
                Ctemp = T
                Ftemp = int(str((Ctemp * 1.8) + 32)[:2])
                self.digital_display.temperature(Ftemp)
                self.updateI2CDisplay(Ftemp,H)
                self.board_led.toggle()

            try:
                if self.exit_btn.triggered():
                    break
                
                socket_connection.settimeout(1.0)
                cl, addr = socket_connection.accept()
                self.ip_address = addr
                print('client connected from', addr)
                cl_file = cl.makefile('rwb', 0)   
                
                while True:
                    line = cl_file.readline()
                    if not line or line == b'\r\n':
                        break            

                response = self.get_html('index.html')  
                response = response.replace('the_temp', str(Ftemp))
                cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
                cl.send(response)
                cl.close()
                
            except OSError as e:
                print(e)

    def updateI2CDisplay(self,temperature,humidity):
        self.i2cdisplay.fill(0)
        self.i2cdisplay.text('Temp: ' + str(temperature) + 'F', 0, 0, 1)
        self.i2cdisplay.text('Humidity: ' + str(humidity) + '%', 0, 10, 1)
        self.i2cdisplay.text('Network:', 0, 30, 1)
        self.i2cdisplay.text(str(self.ip_address), 0, 40, 1)
        self.i2cdisplay.text('K4 To Exit =>', 0, 50, 1)
        self.i2cdisplay.show()

    # Function to load in html page    
    def get_html(self,html_name):
        with open(html_name, 'r') as file:
            html = file.read()
            
        return html    

    def socketConnection(self):
        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        s = socket.socket()
        s.bind(addr)
        s.listen(1)
        print('listening on', addr)
        
        return s

    def networkConnection(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(net_cred.ssid, net_cred.password)

        max_wait = 10
        while max_wait > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            max_wait -= 1
            print('waiting for connection...')    
            time.sleep(1)
        
        if wlan.status() != 3:
            raise RuntimeError('network connection failed')
        else:
            print('connected')
            status = wlan.ifconfig()
            print( 'ip = ' + status[0] )
            self.ip_address = status[0]
