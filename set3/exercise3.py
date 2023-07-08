"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")

    while True:
        lowerBound = input("Enter the lower bound: ")
        try:
            lowerBound = int(lowerBound)
            break
        except ValueError:
            print("Invalid input. Please enter an integer value for the lower bound.")
    
    while True:
        upperBound = input("Enter the upper bound: ")
        try:
            upperBound = int(upperBound)
            if upperBound <= lowerBound:
                print("Upper bound should be greater than the lower bound.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer value for the upper bound.")
    
    print(f"OK then, a number between {lowerBound} and {upperBound} ?")
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)
    
    guessed = False

    while not guessed:
        guessedNumber = input(f"Guess a number: ")
        try:
            guess = int(guessedNumber)
            if guess < lowerBound or guess > upperBound:
                print("Your guess is outside the bounds. Try again.")
            elif guess == actualNumber:
                print(f"You got it!! It was {actualNumber}")
                guessed = True
            elif guess < actualNumber:
                print("Too small, try again.")
            else:
                print("Too big, try again.")
        except ValueError:
            print("Invalid input. Please enter an integer value for your guess. Try again.")

    return "You got it!"
    


if __name__ == "__main__":
    print(advancedGuessingGame())
