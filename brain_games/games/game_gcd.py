"""Contains brain-GCD game."""


import random

import prompt


def generate_numbers():
    """Generate two numbers, return them with their greatest common divisor."""
    number_one = random.randint(1, 100)
    number_two = random.randint(1, number_one)
    divisor = number_two
    while divisor > 1:
        if number_one % divisor == 0 and number_two % divisor == 0:
            return (number_one, number_two, divisor)
        divisor -= 1
    return generate_numbers()


def mix_numbers(result_of_generation):
    """Mix generated numbers and return them with greatest common divisor."""
    (number_one, number_two, divisor) = result_of_generation
    if random.randint(0, 1) == 0:
        return (number_two, number_one, divisor)
    return (number_one, number_two, divisor)


def brain_game_gcd(wins_number):
    """Interact with user and return 'win' or 'lose'."""
    if wins_number == 0:
        print('Find the greatest common divisor of given numbers.')
    (number_one, number_two, divisor) = mix_numbers(generate_numbers())
    print('Question: {0} {1}'.format(number_one, number_two))
    answer = prompt.integer('Your answer: ')
    if answer == divisor:
        return 'win'
    return 'lose', answer, divisor
