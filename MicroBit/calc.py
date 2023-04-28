from microbit import *

second_number = False
first = 0
second = 0


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

def operate():
    if operators_index % len(operators) == 0:
        return first+second
    elif operators_index % len(operators) == 1:
        return first-second
    elif operators_index % len(operators) == 2:
        return first*second
    else:
        return first/second

display.show(0)
while True:
    if accelerometer.was_gesture('shake'):
        if not second_number:
            second_number = True
            numbers_index = 0
            operators_index = 0
            display.show(0)
        else:
            display.show(operate())
            sleep(5000)
            second_number = False
            first = 0
            second = 0
            numbers_index = 0
            display.show(0)
            break
    
    if button_a.is_pressed() and button_b.is_pressed():
        while button_a.is_pressed() or button_b.is_pressed():
            pass
        display.show(Image(operators[operators_index % len(operators)]))
        operators_index += 1

    elif button_a.was_pressed():
        sleep(200)
        if not button_b.was_pressed():
            numbers_index -= 1
            display.show(numbers[numbers_index % len(numbers)])
            if second_number:
                second = numbers[numbers_index % len(numbers)]
            else:
                first = numbers[numbers_index % len(numbers)]
    elif button_b.was_pressed():
        sleep(200)
        if not button_a.was_pressed():
            numbers_index += 1
            display.show(numbers[numbers_index % len(numbers)])
            if second_number:
                second = numbers[numbers_index % len(numbers)]
            else:
                first = numbers[numbers_index % len(numbers)]
