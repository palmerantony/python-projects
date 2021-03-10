# A command line rock paper scissors
#   rock beats scissors
#   scissors beat paper
#   paper beats rock
import random

possibleOptions = ["ROCK", "PAPER", "SCISSORS"]

print("Let's play Rock Paper Scissors!")
print("Choose one of: 'Rock', 'Paper', 'Scissors'")

# all uppercased to make sure we don't care about the case in the user input
playerChoice = input().upper()
computerChoice = random.choice(possibleOptions)

print("You chose: " + playerChoice)
print("Opponent chose: " + computerChoice)

# this is a bit horrendous - at least there aren't too many game states and we know the're a fixed set
if playerChoice == computerChoice:
    print("Draw!")
elif (playerChoice == "ROCK" and computerChoice == "PAPER") or (playerChoice == "PAPER" and computerChoice == "SCISSORS") or (playerChoice == "SCISSORS" and computerChoice == "ROCK"):
    print("You lose!")
elif (playerChoice == "ROCK" and computerChoice == "SCISSORS") or (playerChoice == "PAPER" and computerChoice == "ROCK") or (playerChoice == "SCISSORS" and computerChoice == "PAPER"):
    print("You win... this time")