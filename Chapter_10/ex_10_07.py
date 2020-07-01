'''Write a function to count how many odd numbers are in a list.'''

def countOdd(lst):
    count = 0
    for num in lst:
        if num % 2 != 0:
            count += 1
    return count