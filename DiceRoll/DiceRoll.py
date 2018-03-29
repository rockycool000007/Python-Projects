"""
Title: Dice Roll
Creator: Brittany Gates (github.com/bcgates82 / twitter.com/brittanygates82)
About: Pick a die to roll
"""

import random


# Function for the four-sided dice
def four_sided_dice():
    dice_roll = random.randint(1, 4)
    print('You rolled a {}'.format(dice_roll))
    # Variable and statement that asks the users if they want to roll the same dice again
    roll_dice_again = input('Roll again? Yes or no? ')
    if roll_dice_again == 'y' or roll_dice_again == 'yes':
        four_sided_dice()
    # If the users doesn't want to roll the same dice again, they can go back to the menu
    # and choose another dice
    elif roll_dice_again == 'n' or roll_dice_again == 'no':
        back_to_menu = input('Would you like to go back to the menu? ')
        if back_to_menu == 'y' or back_to_menu == 'yes':
            menu()
        elif back_to_menu != 'y' or back_to_menu != 'yes' or back_to_menu != 'n' or back_to_menu != 'no':
            back_to_menu = input('That is not a valid response. Would you like to ' +
                                 'go back to the menu? Please enter "Yes" or "No." ')
            if back_to_menu == 'y' or back_to_menu == 'yes':
                menu()
            else:
                print('Thanks for rolling!')
        else:
            print('Thanks for rolling!')
    else:
        roll_dice_again = input('That is not a valid response. Do you want to roll again? ' +
                                'Please enter "Yes" or "No." ')
        if roll_dice_again == 'y' or roll_dice_again == 'yes':
            four_sided_dice()
        else:
            print('Thanks for rolling!')


# Function for the six-sided dice
def six_sided_dice():
    dice_roll = random.randint(1, 6)
    print('You rolled a {}'.format(dice_roll))
    # Variable and statement that asks the users if they want to roll the same dice again
    roll_dice_again = input('Roll again? Yes or no? ')
    if roll_dice_again == 'y' or roll_dice_again == 'yes':
        six_sided_dice()
    # If the users doesn't want to roll the same dice again, they can go back to the menu
    # and choose another dice
    elif roll_dice_again == 'n' or roll_dice_again == 'no':
        back_to_menu = input('Would you like to go back to the menu? ')
        if back_to_menu == 'y' or back_to_menu == 'yes':
            menu()
        elif back_to_menu != 'y' or back_to_menu != 'yes' or back_to_menu != 'n' or back_to_menu != 'no':
            back_to_menu = input('That is not a valid response. Would you like to ' +
                                 'go back to the menu? Please enter "Yes" or "No." ')
            if back_to_menu == 'y' or back_to_menu == 'yes':
                menu()
            else:
                print('Thanks for rolling!')
        else:
            print('Thanks for rolling!')
    else:
        roll_dice_again = input('That is not a valid response. Do you want to roll again? ' +
                                'Please enter "Yes" or "No." ')
        if roll_dice_again == 'y' or roll_dice_again == 'yes':
            six_sided_dice()
        else:
            print('Thanks for rolling!')


# Function for the eight-sided dice
def eight_sided_dice():
    dice_roll = random.randint(1, 8)
    print('You rolled a {}'.format(dice_roll))
    # Variable and statement that asks the users if they want to roll the same dice again
    roll_dice_again = input('Roll again? Yes or no? ')
    if roll_dice_again == 'y' or roll_dice_again == 'yes':
        eight_sided_dice()
    # If the users doesn't want to roll the same dice again, they can go back to the menu
    # and choose another dice
    elif roll_dice_again == 'n' or roll_dice_again == 'no':
        back_to_menu = input('Would you like to go back to the menu? ')
        if back_to_menu == 'y' or back_to_menu == 'yes':
            menu()
        elif back_to_menu != 'y' or back_to_menu != 'yes' or back_to_menu != 'n' or back_to_menu != 'no':
            back_to_menu = input('That is not a valid response. Would you like to ' +
                                 'go back to the menu? Please enter "Yes" or "No." ')
            if back_to_menu == 'y' or back_to_menu == 'yes':
                menu()
            else:
                print('Thanks for rolling!')
        else:
            print('Thanks for rolling!')
    else:
        roll_dice_again = input('That is not a valid response. Do you want to roll again? ' +
                                'Please enter "Yes" or "No." ')
        if roll_dice_again == 'y' or roll_dice_again == 'yes':
            eight_sided_dice()
        else:
            print('Thanks for rolling!')


# Function for the ten-sided dice
def ten_sided_dice():
    dice_roll = random.randint(1, 10)
    print('You rolled a {}'.format(dice_roll))
    # Variable and statement that asks the users if they want to roll the same dice again
    roll_dice_again = input('Roll again? Yes or no? ')
    if roll_dice_again == 'y' or roll_dice_again == 'yes':
        ten_sided_dice()
    # If the users doesn't want to roll the same dice again, they can go back to the menu
    # and choose another dice
    elif roll_dice_again == 'n' or roll_dice_again == 'no':
        back_to_menu = input('Would you like to go back to the menu? ')
        if back_to_menu == 'y' or back_to_menu == 'yes':
            menu()
        elif back_to_menu != 'y' or back_to_menu != 'yes' or back_to_menu != 'n' or back_to_menu != 'no':
            back_to_menu = input('That is not a valid response. Would you like to ' +
                                 'go back to the menu? Please enter "Yes" or "No." ')
            if back_to_menu == 'y' or back_to_menu == 'yes':
                menu()
            else:
                print('Thanks for rolling!')
        else:
            print('Thanks for rolling!')
    else:
        roll_dice_again = input('That is not a valid response. Do you want to roll again? ' +
                                'Please enter "Yes" or "No." ')
        if roll_dice_again == 'y' or roll_dice_again == 'yes':
            ten_sided_dice()
        else:
            print('Thanks for rolling!')


# Function for the twelve-sided dice
def twelve_sided_dice():
    dice_roll = random.randint(1, 12)
    print('You rolled a {}'.format(dice_roll))
    # Variable and statement that asks the users if they want to roll the same dice again
    roll_dice_again = input('Roll again? Yes or no? ')
    if roll_dice_again == 'y' or roll_dice_again == 'yes':
        twelve_sided_dice()
    # If the users doesn't want to roll the same dice again, they can go back to the menu
    # and choose another dice
    elif roll_dice_again == 'n' or roll_dice_again == 'no':
        back_to_menu = input('Would you like to go back to the menu? ')
        if back_to_menu == 'y' or back_to_menu == 'yes':
            menu()
        elif back_to_menu != 'y' or back_to_menu != 'yes' or back_to_menu != 'n' or back_to_menu != 'no':
            back_to_menu = input('That is not a valid response. Would you like to ' +
                                 'go back to the menu? Please enter "Yes" or "No." ')
            if back_to_menu == 'y' or back_to_menu == 'yes':
                menu()
            else:
                print('Thanks for rolling!')
        else:
            print('Thanks for rolling!')
    else:
        roll_dice_again = input('That is not a valid response. Do you want to roll again? ' +
                                'Please enter "Yes" or "No." ')
        if roll_dice_again == 'y' or roll_dice_again == 'yes':
            twelve_sided_dice()
        else:
            print('Thanks for rolling!')


# Function for the twenty-sided dice
def twenty_sided_dice():
    dice_roll = random.randint(1, 20)
    print('You rolled a {}'.format(dice_roll))
    # Variable and statement that asks the users if they want to roll the same dice again
    roll_dice_again = input('Roll again? Yes or no? ')
    if roll_dice_again == 'y' or roll_dice_again == 'yes':
        twenty_sided_dice()
    # If the users doesn't want to roll the same dice again, they can go back to the menu
    # and choose another dice
    elif roll_dice_again == 'n' or roll_dice_again == 'no':
        back_to_menu = input('Would you like to go back to the menu? ')
        if back_to_menu == 'y' or back_to_menu == 'yes':
            menu()
        elif back_to_menu != 'y' or back_to_menu != 'yes' or back_to_menu != 'n' or back_to_menu != 'no':
            back_to_menu = input('That is not a valid response. Would you like to ' +
                                 'go back to the menu? Please enter "Yes" or "No." ')
            if back_to_menu == 'y' or back_to_menu == 'yes':
                menu()
            else:
                print('Thanks for rolling!')
        else:
            print('Thanks for rolling!')
    else:
        roll_dice_again = input('That is not a valid response. Do you want to roll again? ' +
                                'Please enter "Yes" or "No." ')
        if roll_dice_again == 'y' or roll_dice_again == 'yes':
            twenty_sided_dice()
        else:
            print('Thanks for rolling!')


# Welcome message and dice selection
def menu():
    print('=' * 40)
    print('Dice Roll\n')
    print('Choose which dice to roll:\n')
    print('1) Four-sided dice\n2) Six-sided dice\n3) Eight-sided dice\n4) Ten-sided dice\n' +
          '5) Twelve-sided dice\n6) Twenty-sided dice')
    print('=' * 40)
    dice_selection = int(input('Enter the number of your selection here: '))
    # Statement that determines and prints the dice roll
    if dice_selection == 1:
        four_sided_dice()
    elif dice_selection == 2:
        six_sided_dice()
    elif dice_selection == 3:
        eight_sided_dice()
    elif dice_selection == 4:
        ten_sided_dice()
    elif dice_selection == 5:
        twelve_sided_dice()
    elif dice_selection == 6:
        twenty_sided_dice()
    else:
        print('That choice is not valid. Please enter a value between 1 and 6')
        dice_selection = int(input('Enter the number of your selection here: '))
        if dice_selection == 1:
            print('You rolled a {}'.format(four_sided_dice()))
        elif dice_selection == 2:
            print('You rolled a {}'.format(six_sided_dice()))
        elif dice_selection == 3:
            print('You rolled a {}'.format(eight_sided_dice()))
        elif dice_selection == 4:
            print('You rolled a {}'.format(ten_sided_dice()))
        elif dice_selection == 5:
            print('You rolled a {}'.format(twelve_sided_dice()))
        elif dice_selection == 6:
            print('You rolled a {}'.format(twenty_sided_dice()))


menu()
