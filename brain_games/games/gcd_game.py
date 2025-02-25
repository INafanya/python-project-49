from brain_games.games_logic import get_randint, start_game

game_info = 'Find the greatest common divisor of given numbers.'


def get_gdc_question_and_answer():
    number1 = get_randint()
    number2 = get_randint()
    gdc = get_gcd(number1, number2)
    return str(f"{number1} {number2}"), str(gdc)
    

def get_gcd(number1, number2):
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1


def start_gcd_game():
    start_game(get_gdc_question_and_answer, game_info)
