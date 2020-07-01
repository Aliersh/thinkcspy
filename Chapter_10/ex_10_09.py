'''Sum up all the negative numbers in a list.'''

def sumNegatives(lst):
    lneg = []
    for num in lst:
        if num < 0:
            lneg.append(num)
    tsum = sum(lneg)
    return tsum