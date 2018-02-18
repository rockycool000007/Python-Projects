# Python-Projects
Python projects I code as I learn the language

I'm currently learning Python as one of my development goals for work. It's a programming language I have been interested in for the past few months but now I'm serious on learning it.

I'm currently using Udemy to learn Python, using this class: Complete Python Masterclass (https://www.udemy.com/python-the-complete-python-developer-course/)

---

## Rock, Paper, Scissors

This is a text-based game I made in JavaScript (source code here: https://github.com/bcgates82/js-projects) when I started learning Web Development in late 2016. Now I'm transforming the game into Python since I'm learning that for work. I chose this game because I believe it's a good way to implement the `if/elif/else` statements and logic.

* 01/06/18: I uploaded the game with some broken logic on detecting when the user enters wrong input. But the game "worked" however.
* 01/07/18: I fixed the broken logic on detecting when the user enters wrong input and it prompts them to inputer either "r," "p," or "s."
* 01/09/18: I'm going to leave the game as it is right now. I don't have the tally part of the game working like I want but that's something I'll work on later. Overall I'm happy with the progress.

**Upcoming Improvements**

*  ~~Add a `while` statement to the `play_again()` function to where the game will ask if you want to play again until the player inputs "n." As of right now the question is only asked once and then the game stops.~~ **I was able to achieve this by removing the `play_again()` function and keep the `if/else` statement indented into the `play_game()` function.**
* Show a running tally of the score, so to speak, for each game the player plays.

---

## Black History Facts Generator

This is a project I made in Febuary 2017 in JavaScript (source code here: https://github.com/bcgates82/js-projects) to provide random Black History Facts for my Twitter feed. I found myself looking up random facts online and thought there had to be a better way.

The project was originally written in JavaScript and used an `array` to hold the facts, and displayed them randomly on a website using jQuery and the `random` and `Math` methods in JavaScript. In Python I'm still selecting the facts randomly using the `random` method.

**Upcoming Improvements**

* ~~Develop a layout for the facts. Right now it's very bare-bones~~
* ~~Have the app crawl for facts online (not sure how to build a crawler but I will learn)~~ I don't have the time at the moment to learn how to do this
* ~~Use the Twitter API to post the facts to my Twitter account (again, I sure how to do that but I'll learn)~~

I'm going to not implement posting the facts to Twitter via an API because it requires for me to make an app on Twitter with a valid website. As of right now I don't have any websites up and running as I closed them down due to time-management purposes. Since I'm busy with work and this class, I'm going to manually posts tweets to my Twitter profile from the app.

---

## Guess The Number

This is a project I had an idea to do at work. Well, part of the project I learned and worked on while taking the Complete Python Masterclass and other parts of it I brainstormed at work. The objective of the game is to guess the random number within a certain number of tries. I added a twist thought: Various difficulties! 

There are 3 difficulties: Easy, Medium and Hard. The difficulties increase the number range and with the Medium and Hard difficulties, ups the number of tries.

I use the `random` class to generate the number to guess. The game runs using `if/else` statements along with a `while` statement to run the guessing until the number of tries are up.

**Upcoming Improvements**
* Improve the redunancy I have in the initial version. I'm not too sure how to use `globals` in Python yet so I'm reusing the same variables in each function for each difficulty.
* ~~Build a "Play Again" function.~~

---

## Word Guess

This is a project I had an idea a few days after starting my Python class but I didn't really work on it until after starting the `dictionaries` portion of the class. 

The game uses a `dictionary` to contain the words which are the `keys` and each words' hint which are the `values`. Then I randomly choose each word for the game by using the `random` class, along with the `list` and `items` methods acting on the dictionary to obtain the key/value pair and placing it into the `answer` and `hint` variables. From there, a `while` statement runs the game until the player guesses the word or the player runs out of tries.
