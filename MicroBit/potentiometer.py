# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    pin0.write_analog(pin2.read_analog())