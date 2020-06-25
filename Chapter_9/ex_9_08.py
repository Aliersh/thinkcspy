'''Write a function that removes all occurrences of a given letter from a string.'''

def remove_letter(theLetter, theString):
    nstring = ''
    for char in theString:
        if char != theLetter:
            nstring = nstring + char
    return nstring

print(remove_letter('a','camila'))