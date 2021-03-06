"""Contains public functions."""

import prompt


def welcome_user():
    """Made to ask name and say hello."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
