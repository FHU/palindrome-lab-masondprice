#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    lower_word = word.lower()
    reverse_word = lower_word[::-1]
    if lower_word == reverse_word and word != "":
        print('True')
    else:
        print(False)

if __name__ == '__main__': 
    #REMOVE PASS AND YOUR CODE GOES HERE
    word = input()
    palindrome(word)
