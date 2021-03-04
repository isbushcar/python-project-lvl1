"""Main game interface."""


import prompt


def game_start():
    """Welcomes user, ask and returns his name."""
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def game_end(game_result, name):
    """Made to get game result and user's name and retur final message."""
    if game_result == 'win':
        print('Congratulations, {0}!'.format(name))
    if game_result[2] == 'lose':
        message = ' is wrong answer ;(. Correct answer was '
        print("'{0}'{1}'{2}'".format(game_result[0], message, game_result[1]))
        print("Let's try again, {0}!".format(name))
