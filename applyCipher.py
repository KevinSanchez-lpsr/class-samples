import string
# applyCipher.py
# A program to encrypt/decrypt user text
# using Caesar's Cipher
# 
# Author: rc.sanchez.kevin [at] leadps.org

# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
def createDictionary(key):
	lowerAlphabet = string.ascii_lowercase
	upperAlphabet = string.ascii_lowercase
	dictionary = {}
	# append letters to dictionary 
	for l in range(0, len(lowerAlphabet)):
		dictionary[upperAlphabet[(key + l) % 26]] = upperAlphabet[l]
	for l in range(0, len(upperAlphabet)):
		dictionary[lowerAlphabet[(key + l) % 26]] = lowerAlphabet[l]
	dictionary[" "] = " "
	return dictionary
	
	

# gets the encrypted message from the user
# arguments: none
# returns: encoded message
def getMessage():
	# asks what message the user wants to decode
	print("Please enter the enoded message:")
	message = raw_input()
	return message

# for each letter in message, decodes and records
# arguments: encoded message, dictionary
# returns: decoded message
def decodeMessage(message, dictionary):
	# variable for word and loop to append message from dictionary
	deMessage = ""
	for i in message:
		deMessage = deMessage + dictionary[i]
	return deMessage

# outputs the decoded message to the terminal
# arguments: decoded message
# returns: none
def printMessage(message):
	# prints the message
	print(message)


# execution starts here

# ask user for key
# code that should be able to run
try:
	print("What key would you like to use to decode?")
	key = int(raw_input())

	dictionary = createDictionary(key)
	encodedMessage = getMessage()
	decodedMessage = decodeMessage(encodedMessage, dictionary)
	print("Here's your new decoded message:")
	printMessage(decodedMessage)
# if there's an error, it gives a message instead of crashing 
except:
	print("Error: This could't be done. Sorry.")
