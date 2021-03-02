"""Contains brain-even game."""


import random
import prompt


def is_even_or_not(number):
    """cheks if number is even and returns yes or no"""
    if number == 0:
        return 'yes'
    if number % 2 == 0:
        return 'yes'
    return 'no'


def get_answer():
    """Gets and returns user's answer"""
    answer = prompt.string('Your answer: ')
    return answer


def main_game_interface():
    """interacts with user"""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    wins_number = 0
    while wins_number < 3:
        random_number = random.randint(0, 1000)
        print('Question: {}'.format(random_number))
        answer = get_answer()
        if answer == is_even_or_not(random_number):
            print('Correct')
            wins_number += 1
        else:
            print('\'{0}\' is wrong answer ;(. Correct answer was \'{1}\'.'.format(answer, is_even_or_not(random_number)))
            return 'lose'
    if wins_number == 3:
        return 'win'
