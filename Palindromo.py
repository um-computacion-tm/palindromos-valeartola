import unittest

#forma recursiva
def palindrome(word):
    word = word.lower()
    word2 = word[::-1]

    if word == word2:
        return True
    else:
        return False

#forma recursiva profe
def palindrome(word):
    if len(word) <= 1:
        return True
    
    if word[0] == word[-1]:
        return palindrome(word[1: -1])
    else:
        return False

#forma iterativa

    


if __name__ == "__main__":
    unittest.main()