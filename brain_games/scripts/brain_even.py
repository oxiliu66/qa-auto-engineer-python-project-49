import random
import prompt

i = 0
print('Answer "yes" if the number is even, otherwise answer "no".')
while i < 3:
    answer = ''
    rundom_num = random.randint(1, 100)
    if rundom_num % 2 == 0:
        answer += 'yes'
    else:
        answer += 'no'
    ask_num = prompt.string('Question: ' + str(rundom_num))
    if ask_num == answer:
        print('Correct!')
    else:
        print(f'{ask_num} is wrong answer ;(. Correct answer was {answer}')
    i+=1