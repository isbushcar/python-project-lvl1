"""Contains brain-GCD game."""


import random

import prompt


def generate_numbers():
    """Generate two numbers, return them with their greatest common divisor."""
    divisor_exists = 0
    while divisor_exists < 1:
        number_one = random.randint(1, 100)
        number_two = random.randint(1, number_one)
        divisor = number_two
        while divisor > 1:
            if number_one % divisor == 0 and number_two % divisor == 0:
                return (number_one, number_two, divisor)
            divisor -= 1


def mix_numbers(result_of_generation):
    """Mix generated numbers and return them with greatest common divisor."""
    (number_one, number_two, divisor) = result_of_generation
    if random.randint(0, 1) == 0:
        return (number_two, number_one, divisor)
    return (number_one, number_two, divisor)


def brain_game_gcd():
    """Interact with user and return 'win' or 'lose'."""
    print('Find the greatest common divisor of given numbers.')
    wins_number = 0
    while wins_number < 3:
        (number_one, number_two, divisor) = mix_numbers(generate_numbers())
        print('Question: {0} {1}'.format(number_one, number_two))
        answer = prompt.integer('Your answer: ')
        if answer == divisor:
            print('Correct')
            wins_number += 1
        else:
            return (answer, divisor, 'lose')
    if wins_number == 3:
        return 'win'
