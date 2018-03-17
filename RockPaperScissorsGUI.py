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
        # The textbox that displays the winner
        winner_text = tkinter.StringVar()
        winner = tkinter.Label(winner_frame, textvariable=winner_text)
        winner_text.set('The computer picks {}'.format(computer_selection) +
                        '\nIt\'s a tie! Play again.')
        winner.grid(row=3, column=0)
    elif player_selection == 'r' and computer_selection == 'Paper':
        # The textbox that displays the winner
        winner_text = tkinter.StringVar()
        winner = tkinter.Label(winner_frame, textvariable=winner_text)
        winner_text.set('The computer picks {}'.format(computer_selection) +
                        '\nPaper covers Rock. You lose!')
        winner.grid(row=3, column=0)
    elif player_selection == 'r' and computer_selection == 'Scissors':
        # The textbox that displays the winner
        winner_text = tkinter.StringVar()
        winner = tkinter.Label(winner_frame, textvariable=winner_text)
        winner_text.set('The computer picks {}'.format(computer_selection) +
                        '\nRock crushes scissors. You win!')
        winner.grid(row=3, column=0)


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
        # The textbox that displays the winner
        winner_text = tkinter.StringVar()
        winner = tkinter.Label(winner_frame, textvariable=winner_text)
        winner_text.set('The computer picks {}'.format(computer_selection) +
                        '\nIt\'s a tie! Play again.')
        winner.grid(row=4, column=0)
    elif player_selection == 'p' and computer_selection == 'Rock':
        # The textbox that displays the winner
        winner_text = tkinter.StringVar()
        winner = tkinter.Label(winner_frame, textvariable=winner_text)
        winner_text.set('The computer picks {}'.format(computer_selection) +
                        '\nPaper covers rock. You win!')
        winner.grid(row=4, column=0)
    elif player_selection == 'p' and computer_selection == 'Scissors':
        # The textbox that displays the winner
        winner_text = tkinter.StringVar()
        winner = tkinter.Label(winner_frame, textvariable=winner_text)
        winner_text.set('The computer picks {}'.format(computer_selection) +
                        '\nScissors cut Paper. You lose!')
        winner.grid(row=4, column=0)


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
        # The textbox that displays the winner
        winner_text = tkinter.StringVar()
        winner = tkinter.Label(winner_frame, textvariable=winner_text)
        winner_text.set('The computer picks {}'.format(computer_selection) +
                        '\nIt\'s a tie! Play again.')
        winner.grid(row=5, column=0)
    elif player_selection == 's' and computer_selection == 'Rock':
        # The textbox that displays the winner
        winner_text = tkinter.StringVar()
        winner = tkinter.Label(winner_frame, textvariable=winner_text)
        winner_text.set('The computer picks {}'.format(computer_selection) +
                        '\nRock crushes Scissors. You lose!')
        winner.grid(row=5, column=0)
    elif player_selection == 's' and computer_selection == 'Paper':
        # The textbox that displays the winner
        winner_text = tkinter.StringVar()
        winner = tkinter.Label(winner_frame, textvariable=winner_text)
        winner_text.set('The computer picks {}'.format(computer_selection) +
                        '\nScissors cut Paper. You win!')
        winner.grid(row=5, column=0)


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

# The frame for the buttons
button_frame = tkinter.Frame(m_window, background='black')
button_frame.grid(row=1, column=0, columnspan=3)

# Player buttons
rock_button = tkinter.Button(button_frame, text='Rock', command=rock)
rock_button.grid(row=0, column=0)
paper_button = tkinter.Button(button_frame, text='Paper', command=paper)
paper_button.grid(row=0, column=1)
scissors_button = tkinter.Button(button_frame, text='Scissors', command=scissors)
scissors_button.grid(row=0, column=2)

# The frame for the winner display text
winner_frame = tkinter.Frame(m_window, background='black')
winner_frame.grid(row=2, column=0, columnspan=3)

m_window.mainloop()
