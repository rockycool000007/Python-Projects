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
        attack_bat(), attack_troll(), attack_slime(), attack_skeleton(), attack_doppelganger():
        These methods attacks the various enemies, and shows how much damage was done if the attack
        is successful.

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

    def attack_troll(self):
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
                    print('-- Your attack is successful, doing {0.damage_dealt} points of '
                          'damage! --\n'.format(self))
                    sleep(3)
                    a_troll.troll_take_damage(10)

    def attack_slime(self):
        if a_slime.hitpoints > 1:
            random_num = random.randint(1, 10)
            if random_num <= 4:
                print('-- Your attack misses! --\n')
                sleep(3)
                a_slime.acid_attack()
            else:
                if a_slime.split() is True:
                    sleep(3)
                    a_slime.slime_take_damage(0)
                else:
                    sleep(3)
                    print('-- Your attack is successful, doing {0.damage_dealt} points of '
                          'damage! --\n'.format(self))
                    sleep(3)
                    a_slime.slime_take_damage(10)

    def attack_skeleton(self):
        if a_skeleton.hitpoints > 1:
            random_num = random.randint(1, 10)
            if random_num <= 4:
                print('-- Your attack misses! --\n')
                sleep(3)
                a_skeleton.bone_throw()
            else:
                print('-- Your attack is successful, doing {0.damage_dealt} points of '
                      'damage! --\n'.format(self))
                sleep(3)
                a_skeleton.skeleton_take_damage(10)

    def attack_doppelganger(self):
        if a_doppelganger.hitpoints > 1:
            random_num = random.randint(1, 10)
            if random_num <= 4:
                print('-- Your attack misses! --\n')
                sleep(3)
                a_doppelganger.all_attacks()
            else:
                print('-- Your attack is successful, doing {0.damage_dealt} points of '
                      'damage! --\n'.format(self))
                sleep(3)
                a_doppelganger.doppelganger_take_damage(10)

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
        bat_take_damage(), troll_take_damage(), slime_take_damage(), skeleton_take_damage(),
        doppelganger_take_damage(): These methods uses the attack() method from the Player super
        class to determine how much damage is done to the various enemies. If the hitpoints are
        less than or equal to 0, then the attack method doesn't run. This is to keep the attack
        method from running one final time when the enemy dies.
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

    def slime_take_damage(self, damage):
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
            a_slime.acid_attack()

    def skeleton_take_damage(self, damage):
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
            a_skeleton.bone_throw()

    def doppelganger_take_damage(self, damage):
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
            a_doppelganger.all_attacks()


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


class Slime(Enemy):

    """
    This is the Slime class that inherits attributes from the Enemy super class

    Methods:
        acid_attack(): This function is used to attack the player. Using a random number,
        the slime blob may or may not bite the player. It calls the take_damage() function in
        the Player super class to remove hitpoints from the player.
        split(): This function determines whether the Slime blocks the player's attack, hence
        not taking damage.
    """

    def __init__(self, name):
        super().__init__(name=name, hitpoints=40, damage_dealt=5)

    def acid_attack(self):
        random_num = random.randint(1, 4)
        if random_num <= 2:
            print('\n** The {0.name} throws acid at you but misses! **\n'.format(self))
            sleep(3)
            player.attack_slime()
        else:
            print('\n** The {0.name} throws acid on you! **\n'.format(self))
            sleep(3)
            player.take_damage(6)
            player.attack_slime()

    def split(self):
        random_num = random.randint(1, 6)
        if random_num <= 2:
            print('** {0.name} tries to split itself to dodge your attack but fails. **\n'.format(self))
            return False
        else:
            print('** The {0.name} splits in half and dodges your attack! **\n'.format(self))
            return True


class Skeleton(Enemy):
    """
    This is the Skeleton class that inherits attributes from the Enemy super class

    Methods:
        bone_throw(): This function is used to attack the player. Using a random number,
        the skeleton may or may not hit the player with a bone. It calls the take_damage()
        function in the Player super class to remove hitpoints from the player.
    """

    def __init__(self, name):
        super().__init__(name=name, hitpoints=40, damage_dealt=5)

    def bone_throw(self):
        random_num = random.randint(1, 4)
        if random_num <= 2:
            print('\n** The {0.name} throws a bone at you but misses! **\n'.format(self))
            sleep(3)
            player.attack_skeleton()
        else:
            print('\n** The {0.name} hits you with a bone! **\n'.format(self))
            sleep(3)
            player.take_damage(5)
            player.attack_skeleton()


class Doppelganger(Enemy):
    """
    This is the Doppelganger class that inherits attributes from the Enemy super class

    Methods:
        Takes the following methods from the other Enemy characters: bite(), punch(), acid_attack(),
        bone_throw().
    """

    def __init__(self, name):
        super().__init__(name=name, hitpoints=100, damage_dealt=8)

    def all_attacks(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            print('\n** The {0.name} morphs into a bat and bites you! **'.format(self))
            sleep(3)
            player.take_damage(2)
            player.attack_doppelganger()
        elif random_num == 2:
            print('\n** The {0.name} attacks you with a sword, dealing {0.damage_dealt} points of '
                  'damage **'.format(self))
            sleep(3)
            player.take_damage(8)
            player.attack_doppelganger()
        elif random_num == 3:
            print('\n** The {0.name} tries to morph but fails. **'.format(self))
            sleep(3)
            player.take_damage(0)
            player.attack_doppelganger()
        elif random_num == 4:
            print('\n** The {0.name} morphs into a troll and punches you! **'.format(self))
            sleep(3)
            player.take_damage(5)
            player.attack_doppelganger()
        elif random_num == 5:
            print('\n** The {0.name} morphs into a slime blob and throws acid on you! **\n'.format(self))
            sleep(3)
            player.take_damage(5)
            player.attack_doppelganger()
        else:
            print('\n** The {0.name} morphs into a skeleton and hits you with a bone! **\n'.format(self))
            sleep(3)
            player.take_damage(5)
            player.attack_doppelganger()


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
a_slime = Slime('Slime Blob')
a_skeleton = Skeleton('Skeleton')
a_doppelganger = Doppelganger('Doppelganger')

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

if third_branch == 1:
    print('\nYou enter the left door and hear it close behind you. You see drops of liquid falling '
          'from the ceiling.')
    sleep(3)
    print('\nYou hold our your hand to catch some of the liquid, but it burns your palm.\nThen you '
          'hear a sloshing sound. As it gets closer and closer, you hold our your torch to see.')
    sleep(3)
    print('\nA {0.name} oozes from the darkness toward you!'.format(a_slime))
    a_slime.acid_attack()
    player.attack_slime()
elif third_branch == 2:
    print('\nYou enter the right door and hear it close behind you. As you take a step forward '
          'a bone flies by your face!')
    sleep(3)
    print('\nA {0.name} walks around the room, pulling bones off of its body, throwing them '
          'at you!'.format(a_skeleton))
    sleep(3)
    a_skeleton.bone_throw()
    player.attack_skeleton()
# Add a test for an else statement for the open chest if the player inputs something wrong
# else:

# The Doppelganger
print('\nWalking to the end of the room, you find a single door in the center of the room.')
sleep(3)
print('\nA bright light pours through the door. You hesitate to enter.')
sleep(3)
print('\n"WHY DO YOU NOT ENTER? DO YOU FEAR TO FACE ME?"')
sleep(3)
print('\nYou take several steps back from the door, drawing your sword.')
sleep(3)
print('\n"COME THROUGH THE DOOR AND FACE ME!"')
sleep(3)
print('\nYou don\'t move.')
sleep(3)
print('\n"FINE! I\'LL COME TO YOU!"')
sleep(3)
print('\nA figure enters through the single door, the door slamming shut behind it.')
sleep(3)
print('\nAs the figure enters into your view, you see the figure looks just like you!\nThe {0.name} '
      'has the same clothes as you, the same satchel and even the same sword.'.format(a_doppelganger))
sleep(3)
print('\n"I WILL END THIS NOW!"')
a_doppelganger.all_attacks()
player.attack_doppelganger()
