#!usr/bin/env python3


"""Brain-progression game."""


from brain_games.game_engine import run_game as game_engine
from brain_games.games import progression


def main():
    """Made to run a brain-progression game."""
    game_engine(progression)
