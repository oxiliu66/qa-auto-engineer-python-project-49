from brain_games import cli

def greet():
    print("Welcome to the Brain Games!")
    user_name = cli.welcome_user()
    return user_name


def main():
    greet()


if __name__ == "__main__":
    main()