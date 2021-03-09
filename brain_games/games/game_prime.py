"""Contains brain-prime game."""


import random

import prompt


def is_prime(number):
    """Made to return 'yes' if number is prime and 'no' if it is not."""
    if number <= 1:
        return 'no'
    divisor = number - 1
    while divisor > 1:
        if number % divisor == 0:
            return 'no'
        divisor -= 1
    return 'yes'


def brain_game_prime(wins_number):
    """Made to show question, ask answer and check if it's correct."""
    if wins_number == 0:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    number = random.randint(0, 100)
    print('Question: {0}'.format(number))
    answer = prompt.string('Your answer: ')
    if answer == is_prime(number):
        return 'win'
    return 'lose', answer, is_prime(number)
