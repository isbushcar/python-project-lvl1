#!usr/bin/env python3


"""Brain-even game."""


from brain_games.game_engine import game_end, game_start
from brain_games.games.game_even import brain_game_even


def main():
    """Made to run a brain-even game."""
    name = game_start()
    game_result = brain_game_even()
    game_end(game_result, name)
