#!usr/bin/env python3


"""Brain-gcd game."""


from brain_games.game_engine import main as game_engine
from brain_games.games import gcd


def main():
    """Made to run a brain-gcd game."""
    game_engine(gcd)
