'''Write a function findHypot. The function will be given the length of two sides of a right-angled 
triangle and it should return the length of the hypotenuse. (Hint: x ** 0.5 will return the square root, 
or use sqrt from the math module)'''

def findHypot(b,c):
    a=((b**2)+(c**2))**(1/2)
    return a

hyp=findHypot(3,2)
print(hyp)