from brain_games.user_communications import welcome, show_question, check_user_answer

from brain_games.math_func import get_randint, is_even


def start_brain_even():
    name = welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers_count = 0
    while correct_answers_count <= 3:
        if correct_answers_count == 3:
            print(f'Congratulations, {name}!')
            break
        else: 
            number = get_randint()
            correct_answer = is_even(number)
            user_answer = show_question(number)
            if check_user_answer(name, user_answer, correct_answer):
                correct_answers_count += 1
            else:
                break
        
#         if user_answer == even:
#             print('Correct!')
#             attempt += 1
#             if attempt == 3:
#                 print(f'Congratulations, {name}!')
#                 break
#         else:
#             print(f"'{user_answer}' is wrong answer ;(\
# . Correct answer was '{even}'.")
#             print(f"Let's try again, {name}!")
            
#             break


if __name__ == '__main__':
    start_brain_even()