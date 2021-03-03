"""Brain-even game."""


from brain_games.game_even import main_game_interface as game_interface
from brain_games.scripts.brain_games import main as brain_games


def main():
    """Made to run a brain-even game."""
    name = brain_games()
    game_result = game_interface()
    if game_result == 'win':
        print('Congratulations, {0}'.format(name))
    if game_result == 'lose':
        print("Let's try again, {0}".format(name))
