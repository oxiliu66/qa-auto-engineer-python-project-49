import random

def even_or_odd():
    num = random.randint(1, 100)
    if num % 2 == 0:
        return str(num), 'yes'
    else:
        return str(num), 'no'

