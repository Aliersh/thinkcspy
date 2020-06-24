'''Now write the function is_odd(n) that returns True when n is odd and False otherwise.'''

def is_odd(n):
    if n%2!=0:
        return True
    else:
        return False

num=is_odd(3)
print(num)