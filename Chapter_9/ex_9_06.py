'''Write a function that reverses its string argument.'''

def reverse(astrg):
    rstrg = ''
    for char in astrg:
        rstrg = char + rstrg
    return rstrg

print(reverse('cami'))