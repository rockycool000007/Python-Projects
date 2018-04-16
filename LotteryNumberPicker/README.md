# Lottery Number Picker

I made this project because I was discussing my Python training with my mom one night and was telling her how I use the `random` module to randomly pick numbers. She plays the Georgia Lottery and asked me if I could make her a lottery number generator. So that's what I did on-and-off on a Saturday.

I created two versions:

* A Georgia Lottery version
   - This version has a GUI version (I created this mostly for my mom who will be using the program).
* A "generic" version for other states
   - No GUI version in the works right now.

To keep from generating duplicate numbers in games that won't allow duplicates, I staggered the ranges in the `random.randint`. ~I can improve this by maybe implementing a `for-loop` but I'm still working out the logic.~ Looks like that thought was wrong. Some testing I ran today using this idea didn't work like I wanted. So for now I'm going to keep the ranges staggered.

### Changes / Updates

* 04/15/18
   - Changed out the `Message` tkinter option for the `Label` option.
   - Made the winning numbers appear underneath the text.
   - Made other style changes to the code.

### Bugs

* None at this time
