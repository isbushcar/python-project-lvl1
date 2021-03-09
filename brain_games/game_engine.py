"""Main game engine."""


import prompt


def game_start():
    """Welcomes user, ask and returns his name."""
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def game_end(game_result, name):
    """Made to get game result and user's name and return final message."""
    if game_result == 'win':
        print('Congratulations, {0}!'.format(name))
    if game_result[0] == 'lose':
        message = ' is wrong answer ;(. Correct answer was '
        print("'{0}'{1}'{2}'.".format(game_result[1], message, game_result[2]))
        print("Let's try again, {0}!".format(name))


def main(game_name):
    """Game engine."""
    name = game_start()
    wins_number = 0
    while wins_number < 3:
        round_result = game_name(wins_number)
        if round_result == 'win':
            print('Correct!')
            wins_number += 1
        else:
            return game_end(round_result, name)
    if wins_number == 3:
        game_end('win', name)
