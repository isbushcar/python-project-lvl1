"""Main game engine."""


import prompt

from brain_games import games


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
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game_name.briefing)
    wins_number = 0
    while wins_number < 3:
        (question, correct_answer) = game_name.play()
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct!')
            wins_number += 1
        else:
            return show_game_result(('lose', user_answer, correct_answer), name)
    if wins_number == 3:
        show_game_result('win', name)
