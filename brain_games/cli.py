"""Contains public functions."""

import prompt


def welcome_user():
    """Asking name and says hello."""
    name = prompt.string('May I have your name?')
    print('Hello, {0}!'.format(name))
    return name
