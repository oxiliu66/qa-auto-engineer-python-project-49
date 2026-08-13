import prompt


def welcome_user():
    ask_a_name = prompt.string("May I have your name? ")
    print("Hello, " + ask_a_name + '!')


