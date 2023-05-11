from microbit import * 
# Servo setup: 
T = 10
b = 0.5
m = 2.5 - b / 1023 - 0
k = pin2.read_analog()
t = m * k + b

while True: 
    pin16.set_analog_period(10)
    pin16.write_analog(75)
    sleep(1000)
    pin16.write_analog(50)
    sleep(1000)
    pin16.write_analog(100)
    sleep(1000)