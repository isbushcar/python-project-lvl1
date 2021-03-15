"""Contains brain-progression game."""

import random

BRIEFING = 'What number is missing in the progression?'


def generate_question_and_answer():  # noqa: WPS210
    """Made to generate progression, hide one number and return both."""
    progression = []
    start_number = random.randint(1, 100)
    progression_step = random.randint(1, 10)
    for index in range(random.randint(5, 10)):
        progression.append(start_number + progression_step * index)
    progression = [str(number) for number in progression]
    hidden_number_index = random.randint(0, len(progression) - 1)
    hidden_number = progression[hidden_number_index]
    progression[hidden_number_index] = '..'
    return ' '.join(progression), hidden_number
