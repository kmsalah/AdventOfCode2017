'''
--- Day 4: High-Entropy Passphrases ---

#PART 1
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

Your puzzle answer was 477.

        _   _
              ((\o/))
         .-----//^\\-----.
         |    /`| |`\    |
         |      | |      |
         |      | |      |
         |      | |      |
         '------===------'

'''



import re
f = open('input.txt')
spreadsheet = []
for line in f:
	spreadsheet.append([x for x in line.split()])

numRows = len(spreadsheet)
# [x//y for x in line for y in line if (x != y and not x%y)]
numValid = 0
'''
for phrase in spreadsheet:
	invalids = []
	invalids = [x for x in phrase for y in phrase if(x=y)]
	print(invalids)
	if len(invalids) == 0:
		numValid += 1
	invalids.clear()
'''
for phrase in spreadsheet:
	invalids = 0
	for i in range(0, len(phrase)):
		for j in range(i+1, len(phrase)):
			if phrase[i] == phrase[j]:
				if i != j:
					invalids += 1
	if invalids == 0:
		    numValid +=1				
print(numValid)


'''
--- Part Two ---

For added security, yet another system policy has been put in place. Now, a valid passphrase must 
contain no two words that are anagrams of each other - that is, a passphrase is invalid 
if any word's letters can be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
Under this new system policy, how many passphrases are valid?
''' 
numValid = 0
for phrase in spreadsheet:
	invalids = 0
	for i in range(0, len(phrase)):
		for j in range(0, len(phrase)):
			if sorted(phrase[i]) == sorted(phrase[j]):
				if i != j:
					invalids +=1
	if invalids == 0:
		numValid += 1
print(numValid)







