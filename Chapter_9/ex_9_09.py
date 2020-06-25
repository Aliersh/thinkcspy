'''Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!).'''

def reverse(astrg):
    rstrg = ''
    for char in astrg:
        rstrg = char + rstrg
    return rstrg

def is_palindrome(myStr):
    rstrg = reverse(myStr)
    if myStr == rstrg:
        return True
    else:
        return False

print(is_palindrome('gala'))