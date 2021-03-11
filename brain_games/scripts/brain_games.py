#!usr/bin/env python3

"""Welcomes user."""

from brain_games.cli import welcome_user


def main():
    """Made to print welcome message and return user's name."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
