from . import brain_games
import prompt
import random

def main():
    brain_games.greet()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        expression = ()