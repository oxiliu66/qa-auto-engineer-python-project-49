import random

import prompt

from . import brain_games

def even_or_odd():
    name = brain_games.greet()
    i = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i < 3:
        answer = ''
        rundom_num = random.randint(1, 100)
        if rundom_num % 2 == 0:
            answer += 'yes'
        else:
            answer += 'no'
        ask_num = print('Question: ' + str(rundom_num))
        answer_number = prompt.string('Your answer: ')
        if answer_number == answer:
            print('Correct!')
        else:
            print(f"'{answer_number}' is wrong answer ;(. Correct answer was '{answer}'\nLet's try again, {name}!")
            break
        i += 1
def main():
    even_or_odd()

if __name__ == "__main__":
    main()