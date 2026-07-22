"""
---- Version 1 ----
This is a small project for number guessing game
I will store a secret number, user will guess the number
    program will provide feedback if user is too low, too high and if they guessed correct
---- version 1.1 ----
Adapted to no longer store a hard coded secret number.
Secret number is imported
User is required to select a difficulty, and a loop is created for invalid responses.
"""

#source ------------------------------------------

import random

#Introduction ------------------------------------
print("="*30)
print("Welcome to Guess the Number!")
print("="*30)
print()
print("Choose your difficulty")
print("Easy")
print("Medium")
print("Hard")
print()

#difficulty Selection ---------------------------

difficulty = (input(f"difficulty: "))

while (difficulty) not in ("Easy", "Medium", "Hard"):
    print("Please select your difficulty. Spell it out as written above")
    difficulty = (input(f"difficulty: "))
    
print("-"*30)
print(f"you've selected: {difficulty}")


if (difficulty) == (f"Easy"):
    secret_number=random.randint(1,25)
    print("I'm thinking of a number between 1 and 25")
elif (difficulty) == (f"Medium"):
    secret_number=random.randint(1,100)
    print("I'm thinking of a number between 1 and 100")
elif (difficulty) == (f"Hard"):
    secret_number=random.randint(1,1000)
    print("I'm thinking of a number between 1 and 1000")
print("Good Luck!")
#number guessing --------------------------------
guess = int(input("guess the number: "))
guess_count = 1


while (guess) != (secret_number):

    if (guess) > (secret_number):
     print("too high!")

    elif (guess) < (secret_number):
        print("Too Low!")

    guess = int(input("guess the number: "))
    guess_count += 1

#results --------------------------------------
print("---------")
print(f"Correct! The answer was {secret_number}!")
print("---------")
print(f"Guess Count: {guess_count}")
print("---------")