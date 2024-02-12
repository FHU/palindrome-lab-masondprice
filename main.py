#REMOVE PASS AND FIX THIS FUNCTIONMom
def palindrome(word):
    lower_word = word.lower()
    reverse_word = lower_word[::-1]
    if lower_word == reverse_word and len(word) != 0:
        return True
    else:
        return False

if __name__ == '__main__': 
    #REMOVE PASS AND YOUR CODE GOES HERE
    word = input()
    print(palindrome(word))
