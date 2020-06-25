'''Assign to a variable in your program a triple-quoted string that contains your favorite paragraph of text 
- perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.
Write a function that counts the number of alphabetic characters (a through z, or A through Z) in your text 
and then keeps track of how many are the letter ‘e’. Your function should print an analysis of the text 
like this:
Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'.'''

str1 = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
deserunt mollit anim id est laborum.'''

import string

def numChar(paragraph): # Function to count the number of character on a paragraph
    count = 0
    for char in paragraph:
        if char == ' ' or char in string.punctuation: # Not count whitespaces and punctuaction
            count = count
        else:
            count += 1
    return count

def howmanyChar(paragraph, character): # Function to count how many of a certain character is in a paragraph
    count = 0
    for char in paragraph:
        if char == character.upper() or char == character.lower(): # Lower and upper case character
            count += 1
    return count

char = 'e'
totalChar = numChar(str1)
totalnChar = howmanyChar(str1,char)
perc = (totalnChar/totalChar)*100

print("Your text contains {} alphabetic characters, of which {} ({:.1f}%) are '{}'.".format(totalChar, totalnChar, perc, char))