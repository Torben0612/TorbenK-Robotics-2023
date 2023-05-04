# Imports go at the top
from microbit import *
import log


# Code in a 'while True:' loop repeats forever
while True:
    @run_every(s=10)
    def log_data():
        log.add({
          'temperature': temperature(),
          'sound': microphone.sound_level(),
          'light': display.read_light_level()
        })
        
    while True:
        sleep(100000)
