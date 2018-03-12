"""
Title: Rock, Paper, Scissors GUI Version
Creator: Brittany Gates (github.com/bcgates82 / twitter.com/brittanygates82)
About: The player chooses either rock, paper or scissors against the computer.
"""

import tkinter
import random


def rock():
    # This block of code determines the computer's selection using the random number generator
    random_num = random.randint(0, 2)
    if random_num == 0:
        computer_selection = 'Rock'
    elif random_num == 1:
        computer_selection = 'Paper'
    else:
        computer_selection = 'Scissors'

    player_selection = 'r'
    if player_selection == 'r' and computer_selection == 'Rock':
        print('The computer picks {}'.format(computer_selection))
        print('It\'s a tie! Play again.')
    elif player_selection == 'r' and computer_selection == 'Paper':
        print('The computer picks {}'.format(computer_selection))
        print('Paper covers Rock. You lose!')
    elif player_selection == 'r' and computer_selection == 'Scissors':
        print('The computer picks {}'.format(computer_selection))
        print('Rock crushes scissors. You win!')


def paper():
    # This block of code determines the computer's selection using the random number generator
    random_num = random.randint(0, 2)
    if random_num == 0:
        computer_selection = 'Rock'
    elif random_num == 1:
        computer_selection = 'Paper'
    else:
        computer_selection = 'Scissors'

    player_selection = 'p'
    if player_selection == 'p' and computer_selection == 'Paper':
        print('The computer picks {}'.format(computer_selection))
        print('It\'s a tie! Play again.')
    elif player_selection == 'p' and computer_selection == 'Rock':
        print('The computer picks {}'.format(computer_selection))
        print('Paper covers rock. You win!')
    elif player_selection == 'p' and computer_selection == 'Scissors':
        print('The computer picks {}'.format(computer_selection))
        print('Scissors cut Paper. You lose!')


def scissors():
    # This block of code determines the computer's selection using the random number generator
    random_num = random.randint(0, 2)
    if random_num == 0:
        computer_selection = 'Rock'
    elif random_num == 1:
        computer_selection = 'Paper'
    else:
        computer_selection = 'Scissors'

    player_selection = 's'
    if player_selection == 's' and computer_selection == 'Scissor':
        print('The computer picks {}'.format(computer_selection))
        print('It\'s a tie! Play again.')
    elif player_selection == 's' and computer_selection == 'Rock':
        print('The computer picks {}'.format(computer_selection))
        print('Rock crushes Scissors. You lose!')
    elif player_selection == 's' and computer_selection == 'Paper':
        print('The computer picks {}'.format(computer_selection))
        print('Scissors cut Paper. You win!')


# def play_again():
#     play_again = input('\nWould you like to play again?\n"Y" for yes or "N" for no: ').lower()
#
#     if play_again == 'y':
#         play_game()
#     else:
#         print('Thanks for playing!')


m_window = tkinter.Tk()

# Setup the main window and frames for the player and computer player
m_window.title('Rock, Paper, Scissors')
m_window.geometry('320x320')
m_window.configure(background='black')

# The text bar at the top that displays the rules
rules_text = tkinter.StringVar()
rules = tkinter.Label(m_window, textvariable=rules_text)
rules_text.set('Defeat the computer by making your selection below\n\nRules:\n' +
               'Rock beats Scissors\nScissors beat Paper\nPaper beats Rock\n\n' +
               'What is your choice? Click the button below.')
rules.grid(row=0, column=0, columnspan=3)

# The text bar that asks for the player's selection
player_button_text = tkinter.StringVar()
player_button = tkinter.Label(m_window, textvariable=player_button_text)
player_button_text.set('')
player_button.grid(row=1, column=0, columnspan=3)

# The frame for the buttons
button_frame = tkinter.Frame(m_window, relief='groove', borderwidth=3, background='black')
button_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=3)

# Player buttons
rock_button = tkinter.Button(button_frame, text='Rock', command=rock)
rock_button.grid(row=0, column=0)
paper_button = tkinter.Button(button_frame, text='Paper')
paper_button.grid(row=0, column=1)
scissors_button = tkinter.Button(button_frame, text='Scissors')
scissors_button.grid(row=0, column=2)

m_window.mainloop()
