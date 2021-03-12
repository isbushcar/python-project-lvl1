#!usr/bin/env python3


"""Brain-progression game."""


from brain_games.game_engine import run_game
from brain_games.games import progression


def main():
    """Made to run a brain-progression game."""
    run_game(progression)
