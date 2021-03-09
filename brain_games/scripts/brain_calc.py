#!usr/bin/env python3


"""Brain-calc game."""


from brain_games.game_engine import main as game_engine
from brain_games.games.game_calc import brain_game_calc


def main():
    """Made to run a brain-calc game."""
    game_engine(brain_game_calc)
