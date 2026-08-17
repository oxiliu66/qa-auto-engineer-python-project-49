from . import brain_games
import prompt
import random

def run_calc():
    name = brain_games.greet()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        expressions = ['+', '-', '*']
        expression = random.choice(expressions)
        print(f'Question: {number1} {expression} {number2}')
        result = 0
        if expression == '+':
            result = number1 + number2
        elif expression == '-':
            result = number1 - number2
        elif expression == '*':
            result = number1 * number2
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'\nLet's try again, {name}!")
            break

def main():
    run_calc()

if __name__ == '__main__':
    main()
