"""
Title: Text Games Collection - Selection Menu
Creator: Brittany Gates (github.com/bcgates82 / twitter.com/brittanygates82)
About: The menu to select which text-based game to play
"""

import GuessTheNumber
import RockPaperScissors
import WordGuess

# List that contains the text-based games the player can choose from
games = ['Guess The Number', 'Rock, Paper, Scissors', 'Word Guess']

# Welcome message
print('=' * 40)
print('Welcome to the Text Games Selection! Text-based games in this collection:\n\n' +
      '1) {}\n2) {}\n3) {}\n'.format(games[0], games[1], games[2]))

# Game selection variable
game_selection = int(input('Enter the number selection here: '))

# Statement that determines which import module to run
if game_selection == 1:
    GuessTheNumber.play()
elif game_selection == 2:
    RockPaperScissors.play()
elif game_selection == 3:
    WordGuess.play()
