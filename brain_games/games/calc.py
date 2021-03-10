"""Contains brain-calc game."""


import random


def play_calc():
    """Generate expression, return string with it and its result."""
    operator_number = random.randint(1, 3)
    if operator_number == 1:
        number_a = random.randint(0, 100)
        number_b = random.randint(0, 100)
        expression_result = number_a + number_b
        expression_string = '{0} + {1}'.format(str(number_a), str(number_b))
        return expression_string, expression_result
    if operator_number == 2:
        number_a = random.randint(0, 100)
        number_b = random.randint(0, number_a)
        expression_result = number_a - number_b
        expression_string = '{0} - {1}'.format(str(number_a), str(number_b))
        return expression_string, expression_result
    if operator_number == 3:
        number_a = random.randint(0, 100)
        number_b = random.randint(0, 10)
        expression_result = number_a * number_b
        expression_string = '{0} * {1}'.format(str(number_a), str(number_b))
        return expression_string, expression_result


def brief_calc():
    """Made to return game briefing."""
    return 'What is the result of the expression?'
