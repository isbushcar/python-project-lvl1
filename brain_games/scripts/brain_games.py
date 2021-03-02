#!usr/bin/env python3

"""Welcomes user."""

from brain_games.cli import welcome_user


def main():
    """Made to print weclome message."""
    print('Weclome to the Brain Games!')
    name = welcome_user()
    return name


if __name__ == '__main__':
    main()
