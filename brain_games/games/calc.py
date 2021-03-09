"""Contains brain-calc game."""


import random

import prompt


def expression_generator():
    """Generate expression, return string with it and its result."""
    operator_number = random.randint(1, 3)
    if operator_number == 1:
        number_a = random.randint(0, 100)
        number_b = random.randint(0, 100)
        expression_result = number_a + number_b
        expression_string = '{0} + {1}'.format(str(number_a), str(number_b))
        return (expression_string, expression_result)
    if operator_number == 2:
        number_a = random.randint(0, 100)
        number_b = random.randint(0, number_a)
        expression_result = number_a - number_b
        expression_string = '{0} - {1}'.format(str(number_a), str(number_b))
        return (expression_string, expression_result)
    if operator_number == 3:
        number_a = random.randint(0, 100)
        number_b = random.randint(0, 10)
        expression_result = number_a * number_b
        expression_string = '{0} * {1}'.format(str(number_a), str(number_b))
        return (expression_string, expression_result)


def brain_game_calc(wins_number):
    """Interacts with user and return win or lose."""
    if wins_number == 0:
        print('What is the result of the expression?')
    (expression_string, expression_result) = expression_generator()
    print('Question: {0}'.format(expression_string))
    answer = prompt.integer('Your answer: ')
    if answer == expression_result:
        return 'win'
    return 'lose', answer, expression_result