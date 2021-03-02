"""brain-even game"""


import brain_games.scripts.brain_games
from brain_games.game_even import *


def main():
    name = brain_games.scripts.brain_games.main()
    game_result = brain_games.game_even.main_game_interface()
    if game_result == 'win':
        print('Congratulations, {}'.format(name))
    if game_result == 'lose':
        print('Let\'s try again, {}'.format(name))
