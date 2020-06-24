'''Write a function, is_prime, that takes a single integer argument and returns True when the argument is 
a prime number and False otherwise.'''

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

pn = is_prime(25)
print(pn)