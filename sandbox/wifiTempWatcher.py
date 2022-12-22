
import network
import socket
import utime as time
import tm1637
from machine import Pin
from PicoDHT22 import PicoDHT22
from secrets import secrets

tm = tm1637.TM1637(clk=Pin(17), dio=Pin(16))
dht_sensor=PicoDHT22(Pin(28,Pin.IN,Pin.PULL_UP),dht11=True)

led1 = Pin(6, Pin.OUT)
led2 = Pin(7, Pin.OUT)    
led3 = Pin(8, Pin.OUT)    
led4 = Pin(9, Pin.OUT)
boardLed = Pin("LED", Pin.OUT)

led1.value(1)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets['ssid'], secrets['pw'])

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')    
    led2.value(1)
    time.sleep(1)
    

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

led3.value(1)

tm.number(1)
Ftemp = 1


# Function to load in html page    
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()
        
    return html


while True:  


    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        cl_file = cl.makefile('rwb', 0)   
        
        led4.value(1)

        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break            

        responseSent = 1

        T,H = dht_sensor.read()
        if T is None:
            print(" sensor error")
        else:
            Ctemp = T
            Ftemp = int(str((Ctemp * 1.8) + 32)[:2])
            tm.temperature(Ftemp)
            boardLed.toggle()

        response = get_html('index.html')  
        response = response.replace('the_temp', str(Ftemp))
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        
    except OSError as e:
        cl.close()
        print('connection closed')


