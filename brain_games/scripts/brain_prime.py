from brain_games.basics import run_game
from brain_games.games.brain_prime_game import prime


def main():
    run_game(prime, 'Answer "yes" if given number is '
                    'prime. Otherwise answer "no".')


if __name__ == "__main__":
    main()