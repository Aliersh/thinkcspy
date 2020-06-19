'''Write a function called mySqrt that will approximate the square root of a number, call it n, 
by using Newton’s algorithm. Newton’s approach is an iterative guessing algorithm where the initial guess 
is n/2 and each subsequent guess is computed using the formula: 
newguess = (1/2) * (oldguess + (n/oldguess)).'''

def mySqrt (n):
    og = n/2
    for i in range(10):
        ng = (1/2) * (og + (n / og))
        og = ng
    return ng

sqrt = mySqrt(130)
print(sqrt)