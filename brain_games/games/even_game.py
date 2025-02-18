from brain_games.games_logic import get_randint, is_even, start_game

game_info = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_number_and_answer():
    number = get_randint()
    # if is_even(number):
    #     answer = 'yes'
    # else:
    #     answer = 'no'
    answer = 'yes' if is_even(number) else 'no'
    return number, answer


def start_even_game():
    start_game(get_number_and_answer, game_info)

    # correct_answers_count = 0
    # while correct_answers_count <= 3:
    #     if correct_answers_count == 3:
    #         print(f'Congratulations, {name}!')
    #         break
    #     else: 
    #         number = get_randint()
    #         correct_answer = is_even(number)
    #         user_answer = show_question(number)
    #         if check_user_answer(name, user_answer, correct_answer):
    #             correct_answers_count += 1
    #         else:
    #             break