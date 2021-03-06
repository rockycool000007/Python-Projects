"""
Title: Lottery Number Picker
Creator: Brittany Gates (github.com/bcgates82 / twitter.com/brittanygates82)
About: Generate hopefully winning lottery numbers for GA Lottery games
"""

import random


# Cash 3 Rules:
# You pick 3 numbers from 0 to 9.
# Duplicate numbers are allowed
def cash_3():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    print('Your Cash 3 Numbers: {}{}{}'.format(num1, num2, num3))
    generate_again = input('\nGenerate more winning numbers for this game? ')
    if generate_again == 'y' or generate_again == 'yes':
        cash_3()
    else:
        back_to_menu = input('\nWould you like to go back to the menu? ')
        if back_to_menu == 'y' or back_to_menu == 'yes':
            menu()
        else:
            print('\n** Good Luck! **')


# Cash 4 Rules:
# You pick 4 numbers from 0 to 9.
# Duplicate numbers are allowed
def cash_4():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    num4 = random.randint(0, 9)
    print('Your Cash 4 Numbers: {}{}{}{}'.format(num1, num2, num3, num4))
    generate_again = input('\nGenerate more winning numbers for this game? ')
    if generate_again == 'y' or generate_again == 'yes':
        cash_4()
    else:
        back_to_menu = input('\nWould you like to go back to the menu? ')
        if back_to_menu == 'y' or back_to_menu == 'yes':
            menu()
        else:
            print('\n** Good Luck! **')


# Fantasy 5 Rules:
# You pick 5 numbers from 1 to 42
# Duplicate numbers are not allowed
def fantasy_5():
    # I divided up the ranges like this to keep from getting duplicate numbers
    num1 = random.randint(1, 9)
    num2 = random.randint(10, 19)
    num3 = random.randint(20, 29)
    num4 = random.randint(30, 36)
    num5 = random.randint(37, 42)
    num_list = sorted([num1, num2, num3, num4, num5])
    print('Your Fantasy 5 Numbers: {} {} {} {} {}'.format(num_list[0], num_list[1], num_list[2], num_list[3],
                                                          num_list[4]))
    generate_again = input('\nGenerate more winning numbers for this game? ')
    if generate_again == 'y' or generate_again == 'yes':
        fantasy_5()
    else:
        back_to_menu = input('\nWould you like to go back to the menu? ')
        if back_to_menu == 'y' or back_to_menu == 'yes':
            menu()
        else:
            print('\n** Good Luck! **')


# Mega Millions Rules:
# You pick 5 numbers from 1 to 70
# You pick 1 MEGA BALL from 1 to 25
# Duplicate numbers are not allowed
def mega_millions():
    # I divided up the ranges like this to keep from getting duplicate numbers
    num1 = random.randint(1, 14)
    num2 = random.randint(15, 29)
    num3 = random.randint(30, 44)
    num4 = random.randint(45, 59)
    num5 = random.randint(60, 70)
    mega_ball = random.randint(1, 25)
    num_list = sorted([num1, num2, num3, num4, num5])
    print('Your Mega Millions Numbers: {} {} {} {} {} [{}]'.format(num_list[0], num_list[1], num_list[2], num_list[3],
                                                                   num_list[4], mega_ball))
    generate_again = input('\nGenerate more winning numbers for this game? ')
    if generate_again == 'y' or generate_again == 'yes':
        mega_millions()
    else:
        back_to_menu = input('\nWould you like to go back to the menu? ')
        if back_to_menu == 'y' or back_to_menu == 'yes':
            menu()
        else:
            print('\n** Good Luck! **')


# Powerball Rules:
# You pick 5 numbers from 1 to 69
# You pick 1 MEGA BALL from 1 to 26
# Duplicate numbers are not allowed
def powerball():
    # I divided up the ranges like this to keep from getting duplicate numbers
    num1 = random.randint(1, 13)
    num2 = random.randint(14, 27)
    num3 = random.randint(28, 39)
    num4 = random.randint(40, 57)
    num5 = random.randint(58, 69)
    power_ball = random.randint(1, 26)
    num_list = sorted([num1, num2, num3, num4, num5])
    print('Your Powerball Numbers: {} {} {} {} {} [{}]'.format(num_list[0], num_list[1], num_list[2], num_list[3],
                                                               num_list[4], power_ball))
    generate_again = input('\nGenerate more winning numbers for this game? ')
    if generate_again == 'y' or generate_again == 'yes':
        powerball()
    else:
        back_to_menu = input('\nWould you like to go back to the menu? ')
        if back_to_menu == 'y' or back_to_menu == 'yes':
            menu()
        else:
            print('\n** Good Luck! **')


# Jumbo Bucks Lotto Rules:
# You pick 6 numbers from 1 to 47
# Duplicate numbers are not allowed
def jumbo_bucks_lotto():
    # I divided up the ranges like this to keep from getting duplicate numbers
    num1 = random.randint(1, 8)
    num2 = random.randint(9, 18)
    num3 = random.randint(19, 27)
    num4 = random.randint(28, 35)
    num5 = random.randint(36, 41)
    num6 = random.randint(42, 47)
    num_list = sorted([num1, num2, num3, num4, num5, num6])
    print('Your Jumbo Bucks Lotto Numbers: {} {} {} {} {} {}'.format(num_list[0], num_list[1], num_list[2], num_list[3],
                                                                     num_list[4], num_list[5]))
    generate_again = input('\nGenerate more winning numbers for this game? ')
    if generate_again == 'y' or generate_again == 'yes':
        jumbo_bucks_lotto()
    else:
        back_to_menu = input('\nWould you like to go back to the menu? ')
        if back_to_menu == 'y' or back_to_menu == 'yes':
            menu()
        else:
            print('\n** Good Luck! **')


# Welcome message and menu
def menu():
    print('=' * 80)
    print('Lottery Number Picker\n\nChoose which game you want numbers generated for:\n')
    print('1) Cash 3\n2) Cash 4\n3) Fantasy 5\n4) Mega Millions\n5) Powerball\n6) Jumbo Bucks Lotto')
    print('=' * 80 + '\n')
    choice = int(input('What is your choice? Enter the number here: '))
    if choice == 1:
        cash_3()
    elif choice == 2:
        cash_4()
    elif choice == 3:
        fantasy_5()
    elif choice == 4:
        mega_millions()
    elif choice == 5:
        powerball()
    elif choice == 6:
        jumbo_bucks_lotto()
    else:
        print('That choice is not valid. Please enter a number between 1 to 5')
        choice = int(input('What is your choice? Enter the number here: '))
        if choice == 1:
            cash_3()
        elif choice == 2:
            cash_4()
        elif choice == 3:
            fantasy_5()
        elif choice == 4:
            mega_millions()
        elif choice == 5:
            powerball()
        elif choice == 6:
            jumbo_bucks_lotto()


menu()
