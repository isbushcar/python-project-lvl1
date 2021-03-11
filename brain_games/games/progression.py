"""Contains brain-progression game."""

import random

BRIEFING = 'What number is missing in the progression?'


def play():
    """Made to generate progression, hide one number and return both."""
    progression = [str(random.randint(1, 100))]
    progression_step = random.randint(1, 10)
    changed_progression = ' '
    for index in range(0, random.randint(5, 10)):
        progression.append(str(int(progression[index]) + progression_step))
    hidden_number = random.randint(0, len(progression) - 1)
    hidden_number, _ = (
        progression.pop(hidden_number),
        progression.insert(hidden_number, '..'),
    )
    return changed_progression.join(progression), hidden_number
