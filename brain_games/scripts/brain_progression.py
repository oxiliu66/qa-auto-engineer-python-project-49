from brain_games.basics import run_game
from brain_games.games.brain_progression_game import progression_calc

def main():
    run_game(progression_calc, 'What number is missing in the progression?')


if __name__ == '__main__':
    main()