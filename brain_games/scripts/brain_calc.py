"""Brain-even game."""


from brain_games.game_interface import game_end, game_start
from brain_games.games.game_calc import brain_game_calc


def main():
    """Made to run a brain-even game."""
    name = game_start()
    game_result = brain_game_calc()
    game_end(game_result, name)
