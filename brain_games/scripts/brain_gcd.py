from brain_games.basics import run_game
from brain_games.games.brain_gcd_game import start_gdc

def main():
    run_game(start_gdc, 'Find the greatest common divisor of given numbers.')


if __name__ == '__main__':
    main()
