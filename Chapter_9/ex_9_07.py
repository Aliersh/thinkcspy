'''Write a function that mirrors its string argument, generating a string containing the original string 
and the string backwards.'''

def mirror(mystr):
    rstrg = ''
    for char in mystr:
        rstrg = char + rstrg
    mir = mystr + rstrg
    return mir

print(mirror('python'))