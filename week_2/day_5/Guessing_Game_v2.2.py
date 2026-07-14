'''
This is going to be a reiteration of the number guessing game with the following requirements.
    Generate a random number between 1 and 100.
    Ask the user to guess.
    If the guess is too high, say "Too high!"
    If the guess is too low, say "Too low!"
    If correct, congratulate the user.
    Count how many guesses it took.
    Allow the user to type "quit" at any time.
    After a win, ask:
        "Would you like to play again? (y/n)"
'''
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
print()
print("Good Luck!      q to quit")
print()

#number guessing --------------------------------
guess_count = 1
while True:
    guess = input("Guess the number: ")
    if guess == "q":
        print("---------")
        print("Quitters never win!")
        print()
        print(f"The answer was {secret_number}!")
        break
    guess = int(guess)
    if (guess) == (secret_number):
        print("---------")
        print("Correct!")
        break
    elif (guess) > (secret_number):
     print("too high!")
    elif (guess) < (secret_number):
        print("Too Low!")
    guess_count += 1



#results --------------------------------------

print("---------")
print(f"Guess Count: {guess_count}")
print("---------")


#Replay? --------------------------------------

Play_Again = input(f"Would you like to play again? (y/n):")

while (Play_Again) == "y":
    print("Starting a new game...")
    #need logic to repeat here
    if (Play_Again) == "n":
        break
print("Thanks for playing!")