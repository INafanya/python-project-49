import prompt

from brain_games.is_even_logic import get_randint, is_even


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempt = 0
    while attempt < 3:
        number = get_randint()
        even = is_even(number)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == even:
            print('Correct!')
            attempt += 1
            if attempt == 3:
                print(f'Congratulations, {name}!')
                break
        else:
            print(f"'{user_answer}' is wrong answer ;(\
. Correct answer was '{even}'.")
            print("Let's try again, {name}!")
            
            break


if __name__ == '__main__':
    main()
