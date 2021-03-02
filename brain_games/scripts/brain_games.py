#!usr/bin/env python

"""Welcomes user."""

from brain_games.cli import welcome_user


def greeting():
    """Made to print weclome message."""
    print('Weclome to the Brain Games!')


if __name__ == '__main__':
    greeting()
    welcome_user()
