# Title: Word Guess
# Creator: Brittany Gates (github.com/bcgates82 / twitter.com/brittanygates82)
# About: The player tries to guess the word before their tries are up.

import random

# Player enters their name
player_name = input("Please enter your name: ")

# Number of tries each player gets
tries = 3

# Greeting and rules of the game
print()
print("Hello, {}! Welcome to Word Guess!".format(player_name))
print("=" * 60)
print("Rules:\n* You have {} tries to guess the word from the hint".format(tries) +
      "\n* Don't worry about case sensitivity")
print("=" * 60)

# Dictionary holding the word and its hint
words = {"butterfly": "One wonders if this fly got its name from landing in a pat of this.",
         "computer": "This objects likes to take a byte of 00111011.",
         "stove": "Across the pond, the appliance is called a 'cooker.'",
         "soda": "In the North, they call his beverage 'pop.'",
         "amazon": "This is the name of a huge rainforest in South America and also an online store."}

# Need to choose one of the words randomly for the game
# answer, hint = random.choice(list(words.items()))
answer, hint = random.choice(list(words.items()))

# This statement displays the hint for the answer
print("Word Hint: " + hint + "\n")

# This statement takes the guess from the player
guess = input("What's your guess? ")

# A "while" statement will run the game
while guess != answer:
    tries -= 1
    print("That's not quite it. Try again!")
    guess = input("What's your guess? ").lower()
    if guess == answer:
        print("That's the word! You're smart!")
        break
    elif tries == 1:
        print("You ran out of tries. The word was {}. Game over!".format(answer))
        break

