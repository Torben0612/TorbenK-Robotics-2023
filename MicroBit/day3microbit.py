# Imports go at the top
from microbit import *

index = 0
# Code in a 'while True:' loop repeats forever
while True:
    if accelerometer.was_gesture("left"):
        index -= 100
    elif accelerometer.was_gesture("right"):
        index += 100
    pin0.write_analog(index % 1024)
