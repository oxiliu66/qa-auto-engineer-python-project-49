from brain_games.basics import run_game
from brain_games.games.brain_even_game import even_or_odd

def main():
    run_game(even_or_odd, 'Answer "yes" if the number is '
                          'even, otherwise answer "no".')
if __name__ == '__main__':
    main()
