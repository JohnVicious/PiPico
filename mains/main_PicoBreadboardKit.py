from machine import Pin, ADC, I2C
from libs.tm1637 import *
from libs.ssd1306 import *
from libs.PicoDHT22 import *
from classes.button import button
from classes.led import led
from classes.buzzer import buzzer
from projects.TransitorTemp import TransitorTemp
from projects.DHTTemp import DHTTemp
from projects.SocketTemperature import SocketTemperature

#SETUP - switches, buzzers, leds, displays, sensors, etc...
board_led = led(Pin("LED", Pin.OUT))
board_buzzer = buzzer(Pin(10, Pin.OUT))
btn1 = button(Pin(2, Pin.IN, Pin.PULL_UP)) #Project A - Temperature Display - Transitor
btn2 = button(Pin(3, Pin.IN, Pin.PULL_UP)) #Project B - Temperature Display - DHT11
btn3 = button(Pin(4, Pin.IN, Pin.PULL_UP)) #Project C - Socket Temperature Display - DHT11
btn4 = button(Pin(5, Pin.IN, Pin.PULL_UP)) #Main Menu -> Reselect project
led1 = led(Pin(6, Pin.OUT))
led2 = led(Pin(7, Pin.OUT))    
led3 = led(Pin(8, Pin.OUT))    
led4 = led(Pin(9, Pin.OUT))
digital_display = TM1637(clk=Pin(17), dio=Pin(16))
transistor_sensor = ADC(26)
dht_sensor=PicoDHT22(Pin(28,Pin.IN,Pin.PULL_UP),dht11=True)
i2cdisplay = SSD1306_I2C(128, 64, I2C(0, sda=Pin(0), scl=Pin(1), freq=400000))

def updateI2CDisplay(i2cdisplay):      
    i2cdisplay.fill(0)
    i2cdisplay.text('Please choose a ', 0, 0, 1)
    i2cdisplay.text('program (K1, K2,', 0, 10, 1)
    i2cdisplay.text('K3 switches)!', 0, 20, 1)
    i2cdisplay.show()

#Main.py has started, show board LED and display
i2cdisplay.fill(0)
i2cdisplay.text('Loading!', 0, 0, 1)
i2cdisplay.show()
digital_display.scroll('ready')
updateI2CDisplay(i2cdisplay)
board_led.on()
print('READY!')


#Wait for a button press to determine which "program" to run
while True:    

    if btn1.triggered(): #Digit display temperature using transitor
        print('Starting project A...')
        led4.on()
        board_buzzer.beep()
        i2cdisplay.fill(0)
        i2cdisplay.text('K4 To Exit =>', 0, 50, 1)
        i2cdisplay.show()
        TransitorTemp(transistor_sensor,digital_display,board_led,btn4).startProject()          
        board_buzzer.beep()
        led4.off()
        print('Exiting project A...')
        i2cdisplay.fill(0)
        i2cdisplay.text('Exiting...', 0, 50, 1)
        i2cdisplay.show()
        digital_display.scroll('ready')
        updateI2CDisplay(i2cdisplay)

    if btn2.triggered(): #Digit display temperature using DHT11
        print('Starting project B...')
        led3.on()
        board_buzzer.beep()
        DHTTemp(dht_sensor,digital_display,i2cdisplay,board_led,btn4).startProject()          
        board_buzzer.beep()
        led3.off()
        print('Exiting project B...')    
        i2cdisplay.fill(0)
        i2cdisplay.text('Exiting...', 0, 50, 1)
        i2cdisplay.show()    
        digital_display.scroll('ready')
        updateI2CDisplay(i2cdisplay)

    if btn3.triggered(): #Digit display temperature using DHT over Socket server
        print('Starting project C...')
        led2.on()
        board_buzzer.beep()  
        SocketTemperature(dht_sensor,digital_display,i2cdisplay,board_led,btn4).startProject()    
        board_buzzer.beep()
        led2.off()
        print('Exiting project C...')  
        i2cdisplay.fill(0)
        i2cdisplay.text('Exiting...', 0, 50, 1)
        i2cdisplay.show()
        digital_display.scroll('ready')
        updateI2CDisplay(i2cdisplay)

