'''Add a print statement to Newton’s sqrt function that prints out better each time it is calculated. 
Call your modified function with 25 as an argument and record the results.'''

def mySqrt (n):
    aprox = n/2
    better = (1/2) * (aprox + (n / aprox))
    while better != aprox:
        aprox = better
        better = (1/2) * (aprox + (n / aprox))
        print(better)
    return better

sqrt = mySqrt(25)
print(sqrt)