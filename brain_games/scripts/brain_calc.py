#!usr/bin/env python3


"""Brain-calc game."""


from brain_games.game_engine import run_game
from brain_games.games import calc


def main():
    """Made to run a brain-calc game."""
    run_game(calc)
