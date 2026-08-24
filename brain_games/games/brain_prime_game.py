import random

def prime():
    answer = ''
    number = random.randint(1, 4000)
    if number <= 1:
        answer = 'no'
    elif number <= 3:
        answer = 'yes'
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            answer = 'no'
            break
        else:
            answer = 'yes'
    return f'{number}', answer
