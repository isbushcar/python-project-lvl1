"""Contains brain-progression game."""

import random

BRIEFING = 'What number is missing in the progression?'


def generate_question_and_answer():
    """Made to generate progression, hide one number and return both."""
    progression = []
    start_number = str(random.randint(1, 100))
    progression_step = random.randint(1, 10)
    for index in range(random.randint(5, 10)):
        progression.append(str(int(start_number) + progression_step * index))
    hidden_number = progression[random.randint(0, len(progression) - 1)]
    progression[progression.index(hidden_number)] = '..'
    return ' '.join(progression), hidden_number
