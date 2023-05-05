# Imports go at the top
from microbit import *
import radio
import speech

radio.on()
radio.config(group=23)

# Code in a 'while True:' loop repeats forever
while True:
    radio.on()
    while True:
        message = radio.receive()
        if message:
            display.scroll(message)
    