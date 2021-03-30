"""Contains brain-calc game."""


import random
from operator import add, mul, sub

BRIEFING = 'What is the result of the expression?'


def generate_question_and_answer():
    """Generate expression, return string with it and its result."""
    num_a = random.randint(0, 100)
    num_b = random.randint(0, 100)
    question_forms = {
        add: '{0} + {1}'.format(num_a, num_b),
        sub: '{0} - {1}'.format(num_a, num_b),
        mul: '{0} * {1}'.format(num_a, num_b),
    }
    operation = random.choice((add, sub, mul))
    return question_forms[operation], calculate_result(num_a, num_b, operation)


def calculate_result(num_a, num_b, operation):
    """Made to return a string with result of operation."""
    return str(operation(num_a, num_b))
