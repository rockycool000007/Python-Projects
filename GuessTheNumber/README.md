## Guess The Number

This is a project I had an idea to do at work. Well, part of the project I learned and worked on while taking the Complete Python Masterclass and other parts of it I brainstormed at work. The objective of the game is to guess the random number within a certain number of tries. I added a twist thought: Various difficulties! 

There are 3 difficulties: Easy, Medium and Hard. The difficulties increase the number range and with the Medium and Hard difficulties, ups the number of tries.

I use the `random` class to generate the number to guess. The game runs using `if/else` statements along with a `while` statement to run the guessing until the number of tries are up.

**Upcoming Improvements**
* ~~Improve the redunancy I have in the initial version. I'm not too sure how to use `globals` in Python yet so I'm reusing the same variables in each function for each difficulty.~~ I learn in class that modifying global variables is frowned upon in Python as it is seen as a `side-effect`. Each function should be self-contained with its variables, so the original code I wrote is corect even though it seems redundant to me.
* ~~Build a "Play Again" function.~~
