#!usr/bin/env python3


"""Brain-calc game."""


from brain_games.game_engine import game_end, game_start
from brain_games.games.game_calc import brain_game_calc


def main():
    """Made to run a brain-calc game."""
    name = game_start()
    game_result = brain_game_calc()
    game_end(game_result, name)
