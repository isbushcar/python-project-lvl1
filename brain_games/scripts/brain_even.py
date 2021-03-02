"""brain-even game"""


import brain_games
from brain_games.game_even import *


brain_games.main()
game_result = game_even.main_game_interface()
if game_result == 'win':
    print('Congratulations, {}'.format(brain_games.name))
if game_result == 'lose':
    print('Let\'s try again, {}'.format(brain_games.name))
