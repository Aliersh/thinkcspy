'''Write a function that removes all occurrences of a string from another string.'''

def remove_all(substr,theStr):
    index = theStr.find(substr)
    if index < 0:
        return theStr
    else:
        if substr in theStr:
            nstr = theStr.replace(substr,'')
            return nstr

print(remove_all('an','banana'))