# A simple programme that will ask a user how they are doing
# then tell them the number of words that they said
print("Hey, how are you doing today?")
response = input()
wordsArray = response.split()
numberOfWords = len(wordsArray)

if(numberOfWords > 10):
    print("Very verbose today! You said " + str(numberOfWords) + " words")
else:
    print("Not so chatty! You said " + str(numberOfWords) + " words")