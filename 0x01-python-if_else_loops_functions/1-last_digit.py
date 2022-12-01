#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    number_1 = number % 10
elif number < 0:
    number_1 = ((number * -1) % 10) * -1


if number_1 > 5:
    print("Last digit of {} is {} and is greater than 5" .format(number, number_1))
elif number_1 == 0:
    print("Last digit of {} is {} and is 0" .format(number, number_1))
else:
    print("Last digit of {} is {} and less than 6 and not 0" .format(number, number_1))
