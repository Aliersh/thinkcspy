'''Sum up all the even numbers in a list.'''

def sumEven(lst):
    lsum = []
    for num in lst:
        if num % 2 == 0:
            lsum.append(num)
    tsum = sum(lsum)
    return tsum