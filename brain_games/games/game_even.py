"""Contains brain-even game."""


import random

import prompt


def is_even(number):
    """Made to check if number is even and return yes or no."""
    if number == 0:
        return 'yes'
    if number % 2 == 0:
        return 'yes'
    return 'no'


def brain_game_even(wins_number):
    """Interact with user and return win or lose."""
    if wins_number == 0:
        print('Answer "yes" if the number is even, otherwise answer "no".')
    random_num = random.randint(0, 100)
    print('Question: {0}'.format(random_num))
    answer = prompt.string('Your answer: ')
    if answer == is_even(random_num):
        return 'win'
    return (answer, is_even(random_num), 'lose')
