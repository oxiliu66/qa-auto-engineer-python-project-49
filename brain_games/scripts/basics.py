import prompt
from brain_games.scripts.brain_games import greet

def run_game(game_question, game_discription):
    name = greet()
    print(game_discription)
    i = 0
    while i < 3:
        question, correct_answer = game_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print(f'Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'\nLet's try again, {name}!")
            return


