from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

#Setting GPIO number standard
GPIO.setmode(GPIO.BCM)

#Hardware
ledRed = LED(17)
ledGreen = LED(27)
ledBlue = LED(22)

##GUI DEFINITIONS
win = Tk()
win.title('LED Toggler')
myFont = tkinter.font.Font(family = 'Helveltica', size = 12, weight = 'bold')

### EVENT FUNCTIONS ###
def ledToggle(color):
    
    if color == 'red':
        led = ledRed
        button = ledRedButton
    elif color == 'green':
        led = ledGreen
        button = ledGreenButton
    else:
        led = ledBlue
        button = ledBlueButton
    
    if led.is_lit:
        led.off()
        button["text"] = 'Turn {} LED on'.format(color)
    else:
        led.on()
        button["text"] = 'Turn {} LED off'.format(color)

### WIDGET ###
ledRedButton = Button(win, text = 'Turn green Led On', font = myFont, command = lambda: ledToggle('red'), bg = 'bisque2', height = 1, width = 24)
ledRedButton.grid(row = 0, column = 1)

ledGreenButton = Button(win, text = 'Turn Led On', font = myFont, command = lambda: ledToggle('green'), bg = 'bisque2', height = 1, width = 24)
ledGreenButton.grid(row = 1, column = 1)

ledBlueButton = Button(win, text = 'Turn Led On', font = myFont, command = lambda: ledToggle('blue'), bg = 'bisque2', height = 1, width = 24)
ledBlueButton.grid(row = 2, column = 1)