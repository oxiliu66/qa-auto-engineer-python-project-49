import random

from brain_games.scripts.basics import run_game


def even_or_odd():
    num = random.randint(1, 100)
    if num % 2 == 0:
        return str(num), 'yes'
    else:
        return str(num), 'no'


def main():
    run_game(even_or_odd, 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == "__main__":
    main()