from brain_games.games_logic import get_randint, is_even, start_game

game_info = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_number_and_answer():
    number = get_randint()
    answer = 'yes' if is_even(number) else 'no'
    return number, answer


def start_even_game():
    start_game(get_number_and_answer, game_info)
    