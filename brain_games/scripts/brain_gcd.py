import random
import prompt
from . import brain_games
from brain_games.scripts.basics import run_game

def find_nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def start_gdc():
    number1 = random.randint(1, 2)
    number2 = random.randint(1, 2)
    correct_answer = str(find_nod(number1, number2))
    return f'{number1} {number2}', correct_answer

def main():
    run_game(start_gdc, 'Find the greatest common divisor of given numbers.')

if __name__ == '__main__':
    main()


