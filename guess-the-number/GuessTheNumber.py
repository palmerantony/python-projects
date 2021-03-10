# Ask a user to guess a number between 1 and 50

import random


def testGuess(secretNumber, playerGuess):
    if secretNumber == playerGuess:
        print("You got it! Amazing guessing")
    else:
        print("Nope... want to guess again?")
        playerGuess = int(input("Next guess: "))
        testGuess(secretNumber, playerGuess)


secretNumber = random.randint(1, 50) #inclusive
print("Let's play a guessing game. I'm thinking of a number between 1 and 50... take a guess what it is.")
playerGuess = int(input("Guess: "))
testGuess(secretNumber, playerGuess)
