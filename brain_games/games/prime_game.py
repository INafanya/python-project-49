from brain_games.games_logic import get_randint, start_game

game_info = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_prime_question_and_answer():
    number = get_randint()
    answer = 'yes' if is_prime_number(number) else 'no'
    return number, answer


def is_prime_number(number):
    if number < 2:
        return False
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1
    return True


def start_prime_game():
    start_game(get_prime_question_and_answer, game_info)
