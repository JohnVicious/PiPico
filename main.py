import tm1637
from classes.button import button
from classes.led import led
from classes.buzzer import buzzer
from machine import Pin, ADC
from PicoDHT22 import PicoDHT22
from projects.TransitorTemp import TransitorTemp
from projects.DHTTemp import DHTTemp
from projects.SocketTemperature import SocketTemperature

board_led = led(Pin("LED", Pin.OUT))
board_buzzer = buzzer(Pin(1, Pin.OUT))
btn1 = button(Pin(2, Pin.IN, Pin.PULL_UP)) #Project A - Temperature Display - Transitor
btn2 = button(Pin(3, Pin.IN, Pin.PULL_UP)) #Project B - Temperature Display - DHT11
btn3 = button(Pin(4, Pin.IN, Pin.PULL_UP)) #Project C - Socket Temperature Display - DHT11
btn4 = button(Pin(5, Pin.IN, Pin.PULL_UP)) #Main Menu -> Reselect project
led1 = led(Pin(6, Pin.OUT))
led2 = led(Pin(7, Pin.OUT))    
led3 = led(Pin(8, Pin.OUT))    
led4 = led(Pin(9, Pin.OUT))

digital_display = tm1637.TM1637(clk=Pin(17), dio=Pin(16))
transistor_sensor = ADC(26)
dht_sensor=PicoDHT22(Pin(28,Pin.IN,Pin.PULL_UP),dht11=True)


#Main.py has started, show board LED and display
digital_display.scroll('ready')
board_led.on()
print('READY!')

#Wait for a button press to determine which "program" to run
while True:    

    if btn1.triggered(): #Digit display temperature using transitor
        print('Starting project A...')
        led4.on()
        board_buzzer.beep()
        TransitorTemp(transistor_sensor,digital_display,board_led,btn4).startProject()          
        board_buzzer.beep()
        led4.off()
        print('Exiting project A...')
        digital_display.scroll('ready')

    if btn2.triggered(): #Digit display temperature using DHT11
        print('Starting project B...')
        led3.on()
        board_buzzer.beep()
        DHTTemp(dht_sensor,digital_display,board_led,btn4).startProject()          
        board_buzzer.beep()
        led3.off()
        print('Exiting project B...')
        digital_display.scroll('ready')

    if btn3.triggered(): #Digit display temperature using DHT over Socket server
        print('Starting project C...')
        led2.on()
        board_buzzer.beep()  
        SocketTemperature(dht_sensor,digital_display,board_led,btn4).startProject()    
        board_buzzer.beep()
        led2.off()
        print('Exiting project C...')
        digital_display.scroll('ready')


