#!usr/bin/env python3


"""Brain-progression game."""


from brain_games.game_engine import main as game_engine
from brain_games.games.progression import brain_game_progression


def main():
    """Made to run a brain-progression game."""
    game_engine(brain_game_progression)
