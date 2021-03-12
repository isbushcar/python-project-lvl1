#!usr/bin/env python3


"""Brain-gcd game."""


from brain_games.game_engine import run_game
from brain_games.games import gcd


def main():
    """Made to run a brain-gcd game."""
    run_game(gcd)
