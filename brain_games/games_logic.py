from random import randint

import prompt

attempt = 3


def get_randint(begin=1, end=100):
    return randint(begin, end)


def is_even(number):
    return number % 2 == 0


def welcome(game_info):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{game_info}')
    return name


def start_game(game_question, game_info):
    name = welcome(game_info)

    for _ in range(attempt):
        question, answer = game_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
