import random


def find_nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def start_gdc():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    correct_answer = str(find_nod(number1, number2))
    return f'{number1} {number2}', correct_answer





