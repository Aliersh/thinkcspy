'''Write a function that removes the first occurrence of a string from another string.'''

def remove(substr,theStr):
    index = theStr.find(substr)
    if index <0:
        return theStr
    else:
        nstr = theStr[:index] + theStr[index + len(substr):]
        return nstr

print(remove('egg','bicycle'))