import random

from brain_games.scripts.basics import run_game


def run_calc():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    expressions = ['+', '-', '*']
    expression = random.choice(expressions)
    result = 0
    if expression == '+':
        result = number1 + number2
    elif expression == '-':
        result = number1 - number2
    elif expression == '*':
        result = number1 * number2
    return f"{number1} {expression} {number2}", str(result)

def main():
    run_game(run_calc, 'What is the result of the expression?')


if __name__ == '__main__':
    main()
