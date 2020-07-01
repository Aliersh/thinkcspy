'''Sum all the elements in a list up to but not including the first even number.'''

def sumUntilEven(lst):
    sum = 0
    index = 0
    while index < len(lst) and lst[index] % 2 != 0:
        sum += lst[index]
        index += 1
    return sum