# Imports go at the top
from microbit import *

index = 0
# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        index -= 100
    elif button_b.was_pressed():
        index += 100
    pin0.write_analog(index % 1024)