from brain_games.games_logic import get_randint, start_game

game_info = 'What number is missing in the progression?'


def get_progression_question_and_answer():
    max_lenght = 15 # get_randint(10)
    first_number = get_randint(1, 20)
    step = get_randint(1, 10)
    position = get_randint(0, max_lenght - 1)
    progression = get_ariphmetic_progression(first_number, step, max_lenght)
    answer = progression[position]
    progression[position] = '..'
    pogression_str = ' '.join(map(str,progression))
    return pogression_str, str(answer)


def get_ariphmetic_progression(first_number, step, max_lenght):
    progression = [first_number + i * step for i in range(max_lenght)]
    return progression

def start_progression_game():
    start_game(get_progression_question_and_answer, game_info)