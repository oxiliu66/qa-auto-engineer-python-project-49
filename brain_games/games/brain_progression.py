import random

from brain_games.scripts.basics import run_game


def progression_calc():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    index = random.randint(5, 15)
    progression = []
    for i in range(index):
        element = start + i * step
        progression.append(str(element))
    hidden_element = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_element])
    progression[hidden_element] = '..'
    question = ' '.join(progression)
    return question, correct_answer


def main():
    run_game(progression_calc, 'What number is missing in the progression?')


if __name__ == '__main__':
    main()

