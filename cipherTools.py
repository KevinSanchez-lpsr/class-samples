# CS 6.5 Tools for Ciphers - Indpendent Practice
# Implement the functions below - when you've finished, all tests should pass
# Author: [your name here]


# import statements here
import string


# calls function to create a list with the letters from a to z
# DOES NOT manually create the list
# use Google and/or Stack Overflow to find how to do this in python!
# returns a list with the lowercase letters a to z
def getLowercaseAlphabet():
    	lowercaseAlpha = list(string.ascii_lowercase)
    	return lowercaseAlpha
    
def getUppercaseAlphabet():
    	uppercaseAlpha = list(string.ascii_uppercase)
    	return uppercaseAlpha
    	
def getReorderedLowercaseAlphabet(key):
    alpha = string.ascii_lowercase
    list = []
    count = 26
    while count > 0:
    	list.append(alpha[(key + count) % 26])
    	count = count - 1
    return list





# DO NOT EDIT THE TESTS BELOW HERE!
# ------------
#

low_alpha = getLowercaseAlphabet()

try:

    if(low_alpha[5] == 'f' and low_alpha[9] == 'j'):
        print("Test 1 passes! getLowercaseAlphabet() is correct.")
    else:
        print("Test 1 fails. getLowercaseAlphabet() needs more work.")
except:
    print("Test 1 fails. getLowercaseAlphabet() needs more work.")



high_alpha = getUppercaseAlphabet()
