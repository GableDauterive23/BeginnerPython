#Imports random number library for Python
import random

#Function that guesses numbers
def guess_number():
    #Randomly chooses a number to guess
    #Guess initially holds an empty value, when the user enters a guess that is used to determine high, low, or equal
    #Attempts counts the number of guesses made
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number_to_guess:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number_to_guess:
            # if guess number is too low it will print this message
            print("Too low!")
        elif guess > number_to_guess:
            # if guess number is too high it will print this message
            print("Too high!")
        else:
            # This message will print when the user makes the correct guess
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
# Calls the function to guess number
guess_number()
