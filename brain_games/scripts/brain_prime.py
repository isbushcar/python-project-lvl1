#!usr/bin/env python3


"""Brain-prime game."""


from brain_games.game_engine import run_game as game_engine
from brain_games.games import prime


def main():
    """Made to run a brain-prime game."""
    game_engine(prime)
