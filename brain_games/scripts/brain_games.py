#!usr/bin/env python3

"""Welcomes user."""

from brain_games.cli import welcome_user


def main():
    """Made to print weclome message and return user's name."""
    print('Weclome to the Brain Games!')
    return welcome_user()


if __name__ == '__main__':
    main()
