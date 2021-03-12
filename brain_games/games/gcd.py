"""Contains brain-GCD game."""


import random

BRIEFING = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    """Generate two numbers, return them with their greatest common divisor."""
    num_one = random.randint(1, 100)
    num_two = random.randint(1, 100)
    divisor = min(num_one, num_two)
    while divisor > 1:
        if num_one % divisor == 0 and num_two % divisor == 0:
            return '{0} {1}'.format(num_one, num_two), divisor
        divisor -= 1
    return generate_question_and_answer()
