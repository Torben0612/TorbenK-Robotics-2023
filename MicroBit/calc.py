from microbit import *
import time

second_number = False

numbers = [0,1,2,3,4,5,6,7,8,9]
numbers_index = 0

PLUS = ('00900:'
        '00900:'
        '99999:'
        '00900:'
        '00900')
MINUS = ('00000:'
         '00000:'
         '99999:'
         '00000:'
         '00000')
TIMES = ('90009:'
         '09090:'
         '00900:'
         '09090:'
         '90009')
DIVIDE = ('00900:'
          '00000:'
          '99999:'
          '00000:'
          '00900')
operators = [PLUS, MINUS, DIVIDE, TIMES]
operators_index = 0

while True:
    if accelerometer.was_gesture('shake'):
        second_number = True
    if button_a.is_pressed() and button_b.is_pressed():
        while button_a.is_pressed() or button_b.is_pressed():
            pass
        operators_index += 1
        display.show(Image(operators[operators_index % len(operators)]))
    elif button_a.was_pressed():
        time.sleep(.2)
        if not button_b.was_pressed():
            numbers_index -= 1
            display.show(numbers[numbers_index % len(numbers)])
    elif button_b.was_pressed():
        time.sleep(.2)
        if not button_a.was_pressed():
            numbers_index += 1
            display.show(numbers[numbers_index % len(numbers)])

def operate(first, second, operator):
    if operators_index % len(operators) == 0:
        return first+second
    elif operators_index % len(operator) == 1:
        return first-second
    elif operator_index % len(operator) == 2:
        return first*second
    else:
        return first/second
