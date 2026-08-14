from brain_games import cli
from . import brain_even

def main():
    print("Welcome to the Brain Games!")
    cli.welcome_user()
    brain_even.even_or_odd()


if __name__ == "__main__":
    main()
