#!usr/bin/env python3


"""Brain-gcd game."""


from brain_games.game_interface import game_end, game_start
from brain_games.games.game_gcd import brain_game_gcd


def main():
    """Made to run a brain-gcd game."""
    name = game_start()
    game_result = brain_game_gcd()
    game_end(game_result, name)
