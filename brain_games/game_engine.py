"""Main game engine."""


import prompt
import brain_games.games


def game_start():
    """Welcomes user, ask and returns his name."""
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def game_end(game_result, name):
    """Made to get game result and user's name and return final message."""
    if game_result == 'win':
        print('Congratulations, {0}!'.format(name))
    if game_result[2] == 'lose':
        message = ' is wrong answer ;(. Correct answer was '
        print("'{0}'{1}'{2}'.".format(game_result[0], message, game_result[1]))
        print("Let's try again, {0}!".format(name))


def main(game_name):
    name = game_start()
    wins_number = 0
    while wins_number < 3:
        (users_answer, correct_answer, round_result) = game_name()
        if round_result == 'win':
            print('Correct!')
            wins_number += 1
        else:
            game_end(users_answer, correct_answer, 'lose')
    if wins_number == 3:
        game_end('win')