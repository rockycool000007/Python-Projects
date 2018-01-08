# Title: Rock, Paper, Scissors
# Creator: Brittany Gates (github.com/bcgates82 / twitter.com/brittanygates82)
# About: The player chooses either rock, paper or scissors to compete against the computer that randomly chooses rock, paper or scissors.

import random

# welcome message and rules
print("Welcome to Rock, Paper, Scissors!\n")
print("Rules:\nRock beats Scissors\nScissors beats Paper\nPaper beats Rock\n")

# The function that runs the game
def play_game():
    # ask for the player's selection
    print("Make your selection:\nR = Rock\nP = Paper\nS = Scissors")
    # variable below takes the player's input and saves it and converts it to lower case
    player_selection = input("Enter your selection here: ").lower()

    # Invalid input from player
    if player_selection != "r" and player_selection != "p" and player_selection != "s":
        print("\nThat is not a valid choice. Please choose \nR = Rock\nP = Paper\nS= Scissors")
        player_selection = input("Enter your selection here: ").lower()

    # This block of code determines the computer's selection using the random number generator
    computer_selection = ""
    random_num = random.randint(0,2)
    if random_num == 0:
        computer_selection = "Rock"
    elif random_num == 1:
        computer_selection = "Paper"
    else:
        computer_selection = "Scissors"

    # Rock section
    if player_selection == "r" and computer_selection == "Rock":
        print("The computer picks {}".format(computer_selection))
        print("It's a tie! Play again.")
    elif player_selection == "r" and computer_selection == "Paper":
        print("The computer picks {}".format(computer_selection))
        print("Paper covers Rock. You lose!")
    elif player_selection == "r" and computer_selection == "Scissors":
        print("The computer picks {}".format(computer_selection))
        print("Rock crushes scissors. You win!")

    # Paper section
    elif player_selection == "p" and computer_selection == "Paper":
        print("The computer picks {}".format(computer_selection))
        print("It's a tie! Play again.")
    elif player_selection == "p" and computer_selection == "Rock":
        print("The computer picks {}".format(computer_selection))
        print("Paper covers rock. You win!")
    elif player_selection == "p" and computer_selection == "Scissors":
        print("The computer picks {}".format(computer_selection))
        print("Scissors cut Paper. You lose!")

    # Scissor section
    elif player_selection == "s" and computer_selection == "Scissor":
        print("The computer picks {}".format(computer_selection))
        print("It's a tie! Play again.")
    elif player_selection == "s" and computer_selection == "Rock":
        print("The computer picks {}".format(computer_selection))
        print("Rock crushes Scissors. You lose!")
    elif player_selection == "s" and computer_selection == "Paper":
        print("The computer picks {}".format(computer_selection))
        print("Scissors cut Paper. You win!")

# Play again function
def play_game_again():
    play_again = input("\nWould you like to play again?\n'Y' for yes or 'N' for no: ").lower()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")

play_game()
play_game_again()