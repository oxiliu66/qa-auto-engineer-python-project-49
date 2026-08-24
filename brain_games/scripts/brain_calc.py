from brain_games.basics import run_game
from brain_games.games.brain_calc_game import run_calc


def main():
    run_game(run_calc, 'What is the result of the expression?')


if __name__ == '__main__':
    main()
