"""
Title: Get To The End
Creator: Brittany Gates (github.com/bcgates82 / twitter.com/brittanygates82)
About: You are in a dungeon filled with enemies, trying to get to the end of it. But, what is at the end?
"""

import random
from time import sleep


# Super class
class Player:
    """
    This is the player class that the person playing the game controls.

    Attributes:
        hitpoints (int): The number of hitpoints the player has
        damage_dealt (int): How much damage the player causes when it hits an enemy with their sword.

    Methods:
        attack_bat(): This function attacks the bat Enemy character, and shows how much damage was done
        if the attack is successful.

        take_damage(): This function subtracts damage from the player, shows how much damage was done to
        the player and displays how many hitpoints are left.
    """

    def __init__(self, hitpoints=100, damage_dealt=10):
        self.hitpoints = hitpoints
        self.damage_dealt = damage_dealt

    def attack_bat(self):
        if a_bat.hitpoints > 1:
            random_num = random.randint(1, 10)
            if random_num <= 4:
                print('-- Your attack misses! --\n')
                sleep(3)
                a_bat.bite()
            else:
                print('-- Your attack is successful, doing {0.damage_dealt} points of '
                      'damage! --\n'.format(self))
                sleep(3)
                a_bat.bat_take_damage(10)

    @staticmethod
    def attack_troll():
        if a_troll.hitpoints > 1:
            random_num = random.randint(1, 10)
            if random_num <= 4:
                print('-- Your attack misses! --\n')
                sleep(3)
                a_troll.punch()
            else:
                if a_troll.block() is True:
                    sleep(3)
                    a_troll.troll_take_damage(0)
                else:
                    sleep(3)
                    a_troll.troll_take_damage(10)

    def take_damage(self, damage):
        self.hitpoints = self.hitpoints - damage
        print('!! You take {} points of damage. You have {} '
              'hitpoints left. !!\n'.format(damage, self.hitpoints))
        sleep(3)


# Super class
class Enemy:
    """
    This is the base class for all enemies in the game.

    Attributes:
        name (str): Either the name of the enemy or the type of the enemy
        hitpoints (int): The number of hitpoints the enemy has
        damage_dealt (int): How much damage the enemy causes when it hits the player with their attack

    Methods:
        bat_take_damage(): This function uses the attack() function from the Player super class to determine
        how much damage is done to the bat enemy. If the hitpoints are below 0, then the bat dies.

        troll_take_damage(): This function uses the attack() function from the Player super class to
        determine how much damage is done to the troll enemy. If the hitpoints are below 0, then the
        troll dies.
    """

    def __init__(self, name, hitpoints, damage_dealt):
        self.name = name
        self.hitpoints = hitpoints
        self.damage_dealt = damage_dealt

    def bat_take_damage(self, damage):
        remaining_points = self.hitpoints - damage
        if remaining_points <= 0:
            self.hitpoints = remaining_points
            print('{0.name} is dead.'.format(self))
            sleep(3)
        else:
            self.hitpoints = remaining_points
            print('{0.name} takes {1} points of damage. {0.name} has {0.hitpoints} '
                  'hitpoints left.\n'.format(self, damage))
            sleep(3)
            player.attack_bat()

    def troll_take_damage(self, damage):
        remaining_points = self.hitpoints - damage
        if remaining_points <= 0:
            self.hitpoints = remaining_points
            print('{0.name} is dead.\n'.format(self))
            sleep(3)
        else:
            self.hitpoints = remaining_points
            print('{0.name} takes {1} points of damage. {0.name} has {0.hitpoints} '
                  'hitpoints left.\n'.format(self, damage))
            sleep(3)
            a_troll.punch()


# Enemy subclass
class Bat(Enemy):

    """
    This is the Bat class that inherits attributes from the Enemy super class

    Methods:
        bite(): This function is used to attack the player. Using a random number, the bat may or may
        not bite the player. It calls the take_damage() function in the Player super class to
        remove hitpoints from the player.
    """

    def __init__(self, name):
        super().__init__(name=name, hitpoints=10, damage_dealt=2)

    def bite(self):
        random_num = random.randint(1, 5)
        if random_num <= 3:
            print('\n** The {0.name} tries to bite you but misses! **\n'.format(self))
            sleep(3)
            player.attack_bat()
        else:
            print('\n** The {0.name} bites you! **\n'.format(self))
            sleep(3)
            player.take_damage(2)


class Troll(Enemy):

    """
    This is the Troll class that inherits attributes from the Enemy super class

    Methods:
        punch(): This function is used to attack the player. Using a random number, the troll may
        or may not punch the player. It calls the take_damage() function in the Player super class to
        remove hitpoints from the player.
        block(): This function determines whether the Troll blocks the player's attack, hence
        not taking damage.
    """

    def __init__(self, name):
        super().__init__(name=name, hitpoints=30, damage_dealt=5)

    def punch(self):
        random_num = random.randint(1, 5)
        if random_num <= 3:
            print('\n** The {0.name} tries to punch you but misses! **\n'.format(self))
            sleep(3)
            player.attack_troll()
        else:
            print('\n** The {0.name} punches you! **\n'.format(self))
            sleep(3)
            player.take_damage(5)
            player.attack_troll()

    def block(self):
        random_num = random.randint(1, 6)
        if random_num <= 2:
            print('** {0.name} tries to block your attack but fails. **\n'.format(self))
            return False
        else:
            print('** The {0.name} blocks your attack! **\n'.format(self))
            return True


# Title screen
print('=' * 16 + '\n')
print('Get To The End')
print('\n' + '=' * 16)
sleep(3)

# Player character creation
player = Player()

# Enemy character creation
a_bat = Bat('Bat')
a_troll = Troll('Troll')

# Introduction
print('\nYou wake up with a start on the floor. You felt something run across your boots.\nYou look around'
      ' the room, catching the glimpse of a rat evading the candle-light, scurrying into a dark corner.\n')
sleep(5)
print('You get to your feet and pick up your gear:\n* A worn satchel\n* A torch\n* A short sword\n')
sleep(5)
print('You sling the satchel across your body, light your torch from the candle and grip your sword.\n')
sleep(5)
print('Your starting hitpoints are {0.hitpoints}, and the damage your sword does is '
      '{0.damage_dealt}.'.format(player) + '\n')
sleep(5)
print('You exit the room through the only open door. You discovered when you first entered the dungeon\n'
      'that each door closes behind you instantly and you cannot open them, no matter how hard you try.\n'
      'So you must make the right decision when you choose a door, lest it be your last decision.\n')
sleep(7)
print('The door slides to a close behind you. Leaving you a choice between two doors:\n1) Left\n2) Right\n')
sleep(5)

# First decision = 2 Doors: Left or Right
first_branch = int(input('Which door do you choose? Enter the number of your choice here: '))
# Left door leads to fighting a bat
if first_branch == 1:
    print('\nYou enter the left door and hear it close behind you. As you take a few steps forward, a '
          'bat swoops out of the corner toward you!')
    sleep(3)
    a_bat.bite()
    player.attack_bat()
# Right door leads to finding a chest with food inside
elif first_branch == 2:
    print('\nYou enter the right door and hear it close behind you.\nYou see an object in the right '
          'corner and walk cautiously to it. You see it\'s a chest. Do you open it?\n'
          '1) Yes\n2) No\n')
    open_chest = int(input('Enter the number of your choice here: '))
    if open_chest == 1:
        print('\nYou find a loaf of bread inside. You kneel next to the chest and eat the bread.')
        sleep(3)
        player.hitpoints += 10
        print('\nYour hitpoints are now {0.hitpoints}.'.format(player))
    elif open_chest == 2:
        print('\nLeery of the bread, you close the chest, deciding not to eat it.')
        sleep(3)
    # Add a test for an else statement for the open chest if the player inputs something wrong
    # else:
# Add a test for an else statement for the first branch if the player inputs something wrong
# else:

# Second decision = 1 Door: Center
print('\nWith the {0.name} dead, you step over the carcass to see one door in the center '
      'of the room.'.format(a_bat))
sleep(3)
print('\nYou enter the door, hearing the familiar noise of the door closing behind you. '
      'Then you hear an unfamiliar noise.')
sleep(3)
print('\nA {0.name} has his back to you, hunched over something. But when the {0.name} sees the '
      'flicker of your torch light he turns around.'.format(a_troll))
sleep(3)
print('\nThe {0.name} screams and rushes toward you!'.format(a_troll))
sleep(3)
a_troll.punch()
player.attack_troll()

# Troll's treasure chest
print('\nWith the {0.name} dead, see what the {0.name} was hunched over: A chest!'.format(a_troll))
sleep(3)
print('\nThe chest is locked with a padlock. You search around for a key.')
sleep(3)
print('\nNot finding one, you check the {0.name}\'s body but can\'t find key on its carcass. '
      'Do want to pry the chest open with your sword?\n1) Yes\n2) No'.format(a_troll))
sleep(3)
pry_chest = int(input('\nEnter the number of your choice here: '))
if pry_chest == 1:
    print('\nIt takes some doing but you are able to break the padlock and open the chest!\n'
          'Inside you find beef jerky and bread. You sit next to the chest and eat the food.')
    sleep(3)
    player.hitpoints += 20
    print('\nUpon standing and gathering your things, you discover prying open the chest damaged '
          'your sword. It now deals 8 points of damage.')
    player.damage_dealt = 8
elif pry_chest == 2:
    print('\nYou leave the chest alone and decide to keep moving, hoping to finally get to the end.')
    sleep(3)
# Add a test for an else statement for the open chest if the player inputs something wrong
# else:

# Third decision = 2 Doors: Left or Right
print('\nWalking to the end of the room, you find two doors:\n1) Left\n2) Right')
sleep(3)
third_branch = int(input('\nWhich door do you choose? Enter the number of your choice here: '))
