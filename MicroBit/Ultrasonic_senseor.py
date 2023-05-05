# Imports go at the top
from microbit import *
from machine import time_pulse_us

#Choose I/O from the pins connected
trig = pin0
echo = pin1

trig.write_digital(0)
trig.read_digital()

# Code in a 'while True:' loop repeats forever
while True:
    trig.write_digital(1)
    trig.write_digital(0)
    
    micros = time_pulse_us(pin1, 1)
    t_echo = micros / 1000000

    dist_cm = (t_echo / 2) * 34300
    display.scroll(str(int(dist_cm)))
    sleep(100)