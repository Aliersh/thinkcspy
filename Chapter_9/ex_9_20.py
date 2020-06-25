'''Write a function called remove_dups that takes a string and creates a new string by only adding those 
characters that are not already present. In other words, there will never be a duplicate letter added to 
the new string.'''

def remove_dups(astring):
    nstr = ''
    for char in astring:
        if char not in nstr:
            nstr = nstr + char
    return nstr

print(remove_dups("mississippi"))