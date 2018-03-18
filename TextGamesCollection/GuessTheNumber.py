"""
Title: Guess The Number
Creator: Brittany Gates (github.com/bcgates82 / twitter.com/brittanygates82)
About: The player tries to guess the number the computer chooses.
There are 3 levels of difficulty: Easy, Medium and Hard.
"""

import random


# The function that runs the game
def play():
    # Function that runs the easy difficulty game
    def easy_diff():
        # Randomly chosen number
        answer = random.randint(1, 10)

        # Difficulty statement
        print('** Easy difficulty **\nNumber range is 1 to 10\n')

        # Player's guess
        guess = int(input('Enter your guess here: '))

        # Number of tries
        tries = 0

        if guess == answer and tries == 0:
            print('Congrats! You guessed the number on the first try!')
        else:
            while guess != answer:
                if guess < answer:
                    tries += 1
                    print('Please guess higher. You have {} tries left.'.format(3 - tries))
                else:
                    tries += 1
                    print('Please guess lower. You have {} tries left.'.format(3 - tries))
                guess = int(input())
                if guess == answer:
                    tries += 1
                    print('That\'s it! You guessed the number in {} tries!'.format(tries))
                    break
                if tries == 2:
                    print('You ran out of tries. The number was {}. Game over!'.format(answer))
                    break

    # Function that runs the medium difficulty game
    def medium_diff():
        # Randomly chosen number
        answer = random.randint(1, 20)

        # Difficulty statement
        print('** Medium difficulty **\nNumber range is 1 to 20\n')

        # Player's guess
        guess = int(input('Enter your guess here: '))

        # Number of tries
        tries = 0

        if guess == answer and tries == 0:
            print('Congrats! You guessed the number on the first try!')
        else:
            while guess != answer:
                if guess < answer:
                    tries += 1
                    print('Please guess higher. You have {} tries left.'.format(5 - tries))
                else:
                    tries += 1
                    print('Please guess lower. You have {} tries left.'.format(5 - tries))
                guess = int(input())
                if guess == answer:
                    tries += 1
                    print('That\'s it! You guessed the number in {} tries!'.format(tries))
                    break
                if tries == 4:
                    print('You ran out of tries. The number was {}. Game over!'.format(answer))
                    break

    # Function that runs the hard difficulty game
    def hard_diff():
        # Randomly chosen number
        answer = random.randint(1, 30)

        # Difficulty statement
        print('** Hard difficulty **\nNumber range is 1 to 30\n')

        # Player's guess
        guess = int(input('Enter your guess here: '))

        # Number of tries
        tries = 0

        if guess == answer and tries == 0:
            print('Congrats! You guessed the number on the first try!')
        else:
            while guess != answer:
                if guess < answer:
                    tries += 1
                    print('\nPlease guess higher. You have {} tries left.'.format(5 - tries))
                else:
                    tries += 1
                    print('\nPlease guess lower. You have {} tries left.'.format(5 - tries))
                guess = int(input())
                if guess == answer:
                    tries += 1
                    print('\nThat\'s it! You guessed the number in {} tries!'.format(tries))
                    break
                if tries == 4:
                    print('\nYou ran out of tries. The number was {}. Game over!'.format(answer))
                    break

    # Function that gives the player a choice to play again
    def play_again():
        play_choice = input('\nWould you like to play again? "Y" for Yes or "N" for No: ').lower()
        if play_choice == 'y':
            print('=' * 80)
            print('Difficulties:\n\n1) Easy: Tries = 3 | Numbers range from 1 to 10\n2) Medium: Tries = 5 | ' +
                  'Numbers range from 1 to 20\n3) Hard: Tries = 5 | Numbers range from 1 to 30')
            print('=' * 80)
            new_difficulty = int(input('Choose your difficulty here: '))

            if new_difficulty == 1:
                easy_diff()
                play_again()
            elif new_difficulty == 2:
                medium_diff()
                play_again()
            elif new_difficulty == 3:
                hard_diff()
                play_again()
        else:
            print('Thanks for playing!')

    # Welcome message, rules and difficulty selection
    print('Welcome to Guess The Number!')
    print()
    print('Rules: Guess the number within the given number of tries.')
    print('=' * 80)
    print('Difficulties:\n\n1) Easy: Tries = 3 | Numbers range from 1 to 10\n2) Medium: Tries = 5 | ' +
          'Numbers range from 1 to 20\n3) Hard: Tries = 5 | Numbers range from 1 to 30')
    print('=' * 80)
    difficulty = int(input('Choose your difficulty here: '))

    # Statement that chooses the correct difficulty function to run based on the player's choice
    if difficulty == 1:
        easy_diff()
    elif difficulty == 2:
        medium_diff()
    elif difficulty == 3:
        hard_diff()

    play_again()


if __name__ == '__main__':
    play()
