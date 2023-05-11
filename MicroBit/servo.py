from microbit import * 
# Servo setup: 
T = 10
b = 0.5
m = 2.5 - b / 1023 - 0
k = pin2.read_analog()
t = m * k + b

def alalog_to_servo(val):
    return int(((val / 1023) * 200) +50)


while True: 
    pin16.set_analog_period(10)
    var = alalog_to_servo(pin2.read_analog())
    pin16.write_analog(var)
