# Asks a user for a phrase as imput asnd returns the acronym

print("Please provide a phrase and I'll return an acronym. For example if you tell me 'United Nations' I'll tell you 'UN'")
phrase = input()
phrase = phrase.upper()
words = phrase.split()

result = ""
for word in words:
    result = result + word[0]

print("Great! The acronym for that is: " + result)