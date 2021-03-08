#!usr/bin/env python3


"""Brain-prime game."""


from brain_games.game_engine import game_end, game_start
from brain_games.games.game_prime import brain_game_prime


def main():
    """Made to run a brain-progression game."""
    name = game_start()
    game_result = brain_game_prime()
    game_end(game_result, name)
