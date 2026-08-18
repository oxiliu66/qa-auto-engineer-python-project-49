import random
import prompt
from . import brain_games

def find_nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def start_gdc():
    name = brain_games.greet()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print(f'Question: {number1}  {number2}')
        correct_answer = str(find_nod(number1, number2))
        player_answer = prompt.string('Your answer: ')
        if correct_answer == player_answer:
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {name}!')

        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct "
                  f"answer was '{correct_answer}'\nLet's try again, {name}!")
            break

def main():
    start_gdc()

if __name__ == '__main__':
    main()


