"""Main game engine."""


import prompt


def get_name():
    """Asks and returns user's name."""
    return prompt.string('May I have your name? ')


def show_game_result(game_result, name):
    """Made to get game result and user's name and return final message."""
    if game_result == 'win':
        print('Congratulations, {0}!'.format(name))
    if game_result[0] == 'lose':
        message = ' is wrong answer ;(. Correct answer was '
        print("'{0}'{1}'{2}'.".format(game_result[1], message, game_result[2]))
        print("Let's try again, {0}!".format(name))


def main(game_name):
    """Game engine."""
    print('Welcome to the Brain Games!')
    name = get_name()
    print('Hello, {0}!'.format(name))
    wins_number = 0
    while wins_number < 3:
        round_result = game_name(wins_number)
        if round_result == 'win':
            print('Correct!')
            wins_number += 1
        else:
            return show_game_result(round_result, name)
    if wins_number == 3:
        show_game_result('win', name)
