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


def main(game_name, brief_name):
    """Game engine."""
    print('Welcome to the Brain Games!')
    name = get_name()
    print('Hello, {0}!'.format(name))
    print(brief_name())
    wins_number = 0
    while wins_number < 3:
        (question, correct_answer) = game_name()
        print('Question: {0}'.format(question))
        users_answer = prompt.string('Your answer: ')
        if users_answer == str(correct_answer):
            print('Correct!')
            wins_number += 1
        else:
            return show_game_result(('lose', users_answer, correct_answer), name)
    if wins_number == 3:
        show_game_result('win', name)
