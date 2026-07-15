'''
Goal: 5 secret numbers are generated from a list
- user gets 3 attempts
- feed back for if correct or game over
'''
# source ------------------------------------

import random
found = False
guess_count = 3

# Answer Generation -------------------------

secret_numbers = []
for _ in range(5):
    secret_numbers.append(random.randint(1, 20))

#print(secret_numbers)

## Game Header -----------------------------
print("="*30)
print("Welcome to Guess the Number!")
print("         VERSION 2")
print("="*30)
print("There are 5 secret numbers,")
print("your goal is to find one of them!")
print()
print("You only get 3 guesses, so choose wisely!")
print("-"*45)

## Guesses defined and feedback ---

guess = int(input("Guess a number between 1 and 20: "))

## need loop for guesses until answer or break if incorrect.

for _ in range (2):
    if guess in secret_numbers:
        print("Correct!")
        break
    else: 
        print("Wrong!")
        print("Guess again!")
        guess_count -= 1
        print(f"Guesses remaining: {guess_count}")
    guess = int(input("Guess a number between 1 and 20: "))

if guess not in secret_numbers:
    print("You're out of guesses!")
    print("Better luck next time!")
