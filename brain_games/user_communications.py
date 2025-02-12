import prompt

def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    return name


def show_question(question):
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    return user_answer


def check_user_answer(name, user_answer, correct_answer):
    if user_answer == correct_answer:
        print('Correct!')
        result = True
    else:
        print(f"'{user_answer}' is wrong answer ;(\
. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        result = False
    return result