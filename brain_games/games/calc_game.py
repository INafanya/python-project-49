from brain_games.games_logic import get_randint, start_game

game_info = 'What is the result of the expression?'


def get_expression():
    number1 = get_randint()
    number2 = get_randint()
    operation = get_operation()
    expression = f'{number1} {operation} {number2}'
    return expression, str(eval(expression))


def get_operation():
    operations = ['+', '-', '*']
    return operations[get_randint(0, len(operations) - 1)]


def start_calc_game():
    start_game(get_expression, game_info)
