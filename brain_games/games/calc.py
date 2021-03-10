"""Contains brain-calc game."""


import operator
import random


def play_calc():
    """Generate expression, return string with it and its result."""
    num_a = random.randint(0, 100)
    num_b = random.randint(0, 100)
    add = ('{0} + {1}'.format(num_a, num_b), operator.add(num_a, num_b))
    sub = ('{0} - {1}'.format(num_a, num_b), operator.sub(num_a, num_b))
    mul = ('{0} * {1}'.format(num_a, num_b), operator.mul(num_a, num_b))
    return random.choice((add, sub, mul))


def brief_calc():
    """Made to return game briefing."""
    return 'What is the result of the expression?'
