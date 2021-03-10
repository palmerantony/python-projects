# A tiny programme that asks a user for a word and then returns it with the first and last letter surrounding the number of removed letters
# for example, 'internationalisation' becomes 'I18N'

print("Please enter a word and I'll give you a stupid abbreviation for it")
word = input().upper()
firstLetter = word[0]
lastLetter = word[len(word)-1]
num = len(word) - 2

result = firstLetter + str(num) + lastLetter

print("The stupid abbreviation is: " + result)
