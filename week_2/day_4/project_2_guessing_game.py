"""
this is a mini project for number guessing game
i will store a secret number, user will guess the number
        program will provide feedback if user is too low, too high and if they guessed correct
"""
secret_number = (7)
guess = int(input("guess the number: "))
guess_count = 1

while (guess) != (secret_number):

    if (guess) > (secret_number):
     print("too high!")

    elif (guess) < (secret_number):
        print("Too Low!")

    guess = int(input("guess the number: "))
    guess_count += 1
print("Correct!")
print(f"Guess Count: {guess_count}")