"""Contains brain-even game."""


import random

BRIEFING = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Made to return True if number is even and False if it is not."""
    return number % 2 == 0


def generate_question_and_answer():
    """Made to return question and correct answer."""
    number = random.randint(0, 100)
    return (number, 'yes') if is_even(number) else (number, 'no')
