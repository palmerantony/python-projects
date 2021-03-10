# Accepts a word from a user and checks whether it is a palindrome

def isPalindrome(word):
    length = len(word) 
    
    # single characters are trivially palindromic
    if length == 1:
        return True

    # we want to go through pairs from the ends
    # casting to an int handles odd-number lengths
    iterations = int(length / 2)
    for n in range(iterations):
        #take the nth letter from each end
        startLetter = word[n]
        endLetter = word[length-n-1]
        if startLetter != endLetter :
            return False
        # else continue
        # if we get here, all the pairs match
        return True

def main():
    print("Hey let's check if a word is a palindrome.")
    word = input("Gimmee your word: ").upper() 
    #uppercased to avoid capitalisation causing issues

    if(isPalindrome(word)):
        print(word + " IS a palindrome")
    else:
        print(word + " IS NOT a palindrome")

main()
