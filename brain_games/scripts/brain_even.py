#!usr/bin/env python3


"""Brain-even game."""


from brain_games.game_engine import run_game
from brain_games.games import even


def main():
    """Made to run a brain-even game."""
    run_game(even)
