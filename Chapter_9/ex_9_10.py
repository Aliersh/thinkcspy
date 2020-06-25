'''Write a function that counts how many non-overlapping occurences of a substring appear in a string.'''

def count(substr,theStr):
    pos = 0
    count = 0
    for char in theStr:
        tchar = theStr[pos:pos + len(substr)] # tchar is a substring with the first character of the iteration + the next characters (total len = len substring)
        if substr == tchar:
            count += 1
            pos += len(substr) # Change pos for no overlapping
        else:
            pos += 1 # Next char for substring
    return count


print(count('ana','banana'))
