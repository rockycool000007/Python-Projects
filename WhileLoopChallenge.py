import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))

guess = int(input())

tries = 0

quit_game = 0

if guess == answer and tries == 0:
    print("You guessed the number on the first try!")
elif guess == quit_game:
    print("Game Over")
else:
    while guess != answer:
        if guess < answer:
            print("Please guess higher.")
            tries += 1
        else:
            print("Please guess lower.")
            tries += 1
        guess = int(input())
        if guess == answer:
            tries += 1
            print("You guessed the number in {} tries!".format(tries))
