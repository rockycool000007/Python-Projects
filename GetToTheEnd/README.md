# Get To The End

This is a project I'm slowly working on to practice my Object Oriented Programming (OOP) that I'm learning in my Python class.

This project is a text-base adventure game where you fight monsters in various rooms and try to get to the end. You have to make decisions on where you go and how to progress.

---

### Changes / Updates

* 5/20/18:
   - I created the validation and/or tests for the `else` statements when the player had to make a decision to catch if the player inputs an invalid number. I did this by creating functions for the two room branches and using a `while` loop in the `else` statement to catch wrong inputs.

* 5/19/18:
   - Created the `Doppelganger` class along with the new Doppelganger enemy the play has to fight (this is the final enemy or final boss).
   - Updated the doc strings for the Player and Enemy super classes to encompass all of the methods used.

* 5/16/18:
   - Created the `Skeleton` class along with the new Skeleton enemy the player has to fight.
   - Finished the third branch of the rooms for the player.
   - Updated the doc strings for the Player and Enemy super classes to encompass all of the methods used.

* 5/15/18:
   - Created the `Slime` class along with the new Slime Blob enemy the player has to fight.
   - Started work on the third branch of rooms for the player.
   - Changed the `attack_troll` static method to a regular method because I forgot that I need to show the amount of damage dealt from the player.

* 5/14/18:
   - Created the decision on whether to open the treasure after defeating the troll.
   - Started working on the third branch of the dungeon.

* 5/13/18:
   - Corrected some incorrectly formed logic that was causing the game to attack both enemies at once.
   - Added a test to both the `attack_bat()` and `attack_troll()` methods so if the Bat's and Troll's hitpoints are less than 1, the methods will not run.
   - For the `Troll` class, I created the `block` method which can block the player's attacks randomly.
   - Fixed typos and cleaned up formmatting in various places.


### Bugs

* 5/14/18:
   ~~- Not exactly a bug, but I need to create validation and/or tests for the `else` statements to catch if the player inputs a wrong number. I haven't figured out the logic for that yet.~~
