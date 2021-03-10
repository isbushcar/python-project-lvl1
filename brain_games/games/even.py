"""Contains brain-even game."""


import random


def play():
    """Made to return question and correct answer."""
    number = random.randint(0, 100)
    if number == 0 or number % 2 == 0:
        return number, 'yes'
    return number, 'no'


briefing = 'Answer "yes" if the number is even, otherwise answer "no".'
