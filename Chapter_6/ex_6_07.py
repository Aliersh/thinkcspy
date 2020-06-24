'''Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and including n. 
So sumTo(10) would be 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2.'''

def sumTo(n):
    result=(n*(n+1))/2
    return result

t=sumTo(10)
print(t)