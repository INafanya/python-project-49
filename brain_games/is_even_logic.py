from random import randint


def get_randint():
    return randint(0, 100)


def is_even(number):
    result = number % 2
    if result == 0:
        return 'yes'
    else:
        return 'no'