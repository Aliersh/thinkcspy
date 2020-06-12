'''Modify is_odd so that it uses a call to is_even to determine if its argument is an odd integer.'''

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

def is_odd(n):
    if is_even(n)==True:
        return False
    else:
        return True

num=is_odd(4)
print(num)