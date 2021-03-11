"""Main game engine."""

import prompt


def run_game(game_name):
    """Game engine. Runs game and returns it's result."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game_name.BRIEFING)
    wins_number = 0
    while wins_number < 3:
        (question, correct_answer) = game_name.play()
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct!')
            wins_number += 1
        else:
            print(
                "'{0}' is wrong answer ;(. Correct answer was '{1}'.".format
                (user_answer, correct_answer),
            )
            print("Let's try again, {0}!".format(name))
            return
    if wins_number == 3:
        print('Congratulations, {0}!'.format(name))
        return
