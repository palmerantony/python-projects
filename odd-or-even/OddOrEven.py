# A simple programme to tell a user if a number is odd or even
print("Hi! What number are you thinking of today?")

# input() is a built in function to accept console input
numberAsString = input()
print("Great, your number was: " + numberAsString)

number = int(numberAsString)
if number % 2 == 0:
    print("Your number is EVEN!")
else: 
    print("Your number is ODD!")
