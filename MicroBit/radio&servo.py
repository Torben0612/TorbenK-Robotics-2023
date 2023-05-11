from microbit import *
import tradio
radio.config(group=23)
radio.on()
pin16.set_analog_period(10)

while True:
    message = radio.receive()
    if message:
        pin16.write_analog(int(message))