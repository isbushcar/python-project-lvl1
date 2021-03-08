#!usr/bin/env python3


"""Brain-progression game."""


from brain_games.game_engine import game_end, game_start
from brain_games.games.game_progression import brain_game_progression


def main():
    """Made to run a brain-progression game."""
    name = game_start()
    game_result = brain_game_progression()
    game_end(game_result, name)
