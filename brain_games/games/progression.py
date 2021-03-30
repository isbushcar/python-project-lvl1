"""Contains brain-progression game."""

import random

BRIEFING = 'What number is missing in the progression?'


def generate_question_and_answer():  # noqa: WPS210
    """Made to generate question and answer."""
    start_number = random.randint(1, 100)
    progression_step = random.randint(1, 10)
    progression_length = random.randint(5, 10)
    progression = generate_progression(
        start_number, progression_step, progression_length,
    )
    return hide_number(progression)


def generate_progression(start_number, step, length):
    """Made to generate progression, hide one number and return both."""
    progression = []
    for index in range(length + 1):
        progression.append(start_number + step * index)
    return [str(number) for number in progression]


def hide_number(progression):
    """Made to return strings with changed progression and hidden number."""
    hidden_number_index = random.randint(0, len(progression) - 1)
    hidden_number = progression[hidden_number_index]
    progression[hidden_number_index] = '..'
    return ' '.join(progression), hidden_number
