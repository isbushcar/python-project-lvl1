"""Contains brain-progression game."""


import random

import prompt


def generate_progression():
    """Generate progression and return it."""
    progression_length = random.randint(5, 10)
    progression_step = random.randint(1, 10)
    current_number = random.randint(1, 10)
    index_number = 2
    progression = (current_number,)
    while index_number <= progression_length:
        current_number += progression_step
        progression += (current_number,)
        index_number += 1
    return progression


def hide_number(progression):
    """Hides number in progression and returns it with hidden number."""
    number_to_hide = random.randint(0, len(progression) - 1)
    hidden_number = progression[number_to_hide]
    index_number = 0
    changed_progression = ''
    while index_number < len(progression):
        if index_number == number_to_hide:
            changed_progression = '{0}.. '.format(changed_progression)
            index_number += 1
        else:
            changed_progression += '{0} '.format(str(progression[index_number]))
            index_number += 1
    changed_progression = changed_progression[:len(changed_progression) - 1]
    return changed_progression, hidden_number


def brain_game_progression(wins_number):
    """Interacts with user and returns 'win' or 'lose'."""
    if wins_number == 0:
        print('What number is missing in the progression?')
    (progression, hidden_number) = hide_number(generate_progression())
    print('Question: {0}'.format(str(progression)))
    answer = prompt.integer('Your answer: ')
    if answer == hidden_number:
        return 'win'
    return 'lose', answer, hidden_number
