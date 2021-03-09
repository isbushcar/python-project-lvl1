#!usr/bin/env python3


"""Brain-even game."""


from brain_games.game_engine import main as game_engine
from brain_games.games.game_even import brain_game_even


def main():
    """Made to run a brain-even game."""
    game_engine(brain_game_even)
