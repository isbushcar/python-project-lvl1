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


def main_game_interface():
    """Interacts with user and return win or lose."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    wins_number = 0
    while wins_number < 3:
        random_num = random.randint(0, 1000)
        print('Question: {0}'.format(random_num))
        answer = prompt.string('Your answer: ')
        if answer == is_even(random_num):
            print('Correct')
            wins_number += 1
        else:
            message = ' is wrong answer ;(. Correct answer was '
            print("'{0}'{1}'{2}'".format(answer, message, is_even(random_num)))
            return 'lose'
    if wins_number == 3:
        return 'win'
