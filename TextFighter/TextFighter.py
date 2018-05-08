"""
Title: Text Fighter
Creator: Brittany Gates (github.com/bcgates82 / twitter.com/brittanygates82)
Rules: The player chooses one of four fighters to compete against the computer's fighter.
"""

import random


class Fighter:

    """
    Base class for the fighters the computer and the player can choose.
    Both the player's fighter and the computer's fighter can be the same.

    Attributes:
        name (str): The name of the player fighter.
        special (str): The name of the player fighter's special move.
        hit_points (int): The default hit points for the player fighter.
        lives (int): The default lives for the computer fighter.

    Methods:"
        fight(): This method runs the match between the computer player and the human player.
    """

    def __init__(self, name, special, hit_points=100, lives=1, kick=30, punch=20, special_damage=50):
        self.name = name
        self.special = special
        self.hit_points = hit_points
        self.lives = lives
        self.kick = kick
        self.punch = punch
        self.special_damage = special_damage

    def __str__(self):
        return '{0.name} | Special: {0.special} | Hit Points: {0.hit_points} | ' \
               ' Lives: {0.lives}'.format(self)


# The function that randomly picks the computer fighter
def computer_fighter_pick():
    random_num = random.randint(0, 3)
    if random_num == 0:
        return jyu
    elif random_num == 1:
        return ben
    elif random_num == 2:
        return shun_li
    else:
        return yuile


# The function that allows the player to choose their fighter
def player_fighter_pick():
    player_choice = int(input('Choose your fighter:\n\n1) Jyu\n2) Ben\n3) Shun Li\n'
                              '4) Yuile\n\nEnter your choice here: '))
    if player_choice == 1:
        print('xXx Your choice is {} xXx'.format(jyu))
        return jyu
    elif player_choice == 2:
        print('xXx Your choice is {} xXx'.format(ben))
        return ben
    elif player_choice == 3:
        print('xXx Your choice is {} xXx'.format(shun_li))
        return shun_li
    elif player_choice == 4:
        print('xXx Your choice is {} xXx'.format(yuile))
        return yuile
    else:
        if player_choice >= 5:
            print('\n*** That is not a valid choice. Please enter a number '
                  'from the choices above. ***\n')
            player_fighter_pick()


# The function that controls the fight
def fight():
    print('*** Your opponent is {}. ***'.format(computer_fighter_pick()))
    player_move = input('\nYou get the first strike! Pick your move:\n'
                        '"P" for Punch\n"K" for Kick\n"S" for Special Move\n'
                        'Enter your choice here: ').lower()
    if player_move == 'p':
        # run function to determine hit or miss
        pass
    elif player_move == 'k':
        # run function to determine hit or miss
        pass
    elif player_move == 's':
        # run function to determine hit or miss
        pass
    else:
        print('\nxXx That is not a valid choice. Please enter a number '
              'from the choices above. xXx\n')
        fight()


# The function that determines the player's move hits the computer fighter
def player_move_hit_or_miss():
    hit_counter = 5  # The number of the human fighter's hits
    random_num = random.randint(0, 5)
    # If the random number is less than or equal to 2, the player hits the computer
    if random_num <= 2:
        print('Hit! You have {} hits left.'.format(hit_counter - 1))
        # Make a function that subtracts damage from the computer fighter's health
        fight()
    else:
        print('Miss! You have {} hits left.'.format(hit_counter - 1))
        fight()


# The fighters the computer and the player can choose from
jyu = Fighter('Jyu', 'Dragon Punch')
ben = Fighter('Ben', 'Flaming Hurricane Kick')
shun_li = Fighter('Shun Li', 'Lighting Kick')
yuile = Fighter('Yuile', 'Flash Kick')

# Welcome message and rules
print('=' * 80)
print('Welcome to Text Fighter!\n')
print('Rules: Choose your fighter and try to defeat your opponent within 5 hits.')
print('=' * 80 + '\n')


computer_fighter_pick()
player_fighter_pick()
fight()
