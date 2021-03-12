"""Contains brain-prime game."""


import random

BRIEFING = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer():
    """Made to return number and 'yes' if it is prime or 'no' if it is not."""
    number = random.randint(0, 100)
    if number <= 1:
        return number, 'no'
    divisor = number // 2
    while divisor > 1:
        if number % divisor == 0:
            return number, 'no'
        divisor -= 1
    return number, 'yes'
