'''Write a function called myPi that will return an approximation of PI (3.14159…). 
Use the Leibniz approximation.'''

def myPi(n):
    pi=0
    sign=1
    den=1 #Denominator
    for i in range(n):
        pi=pi+(sign/den)
        den=den+2
        sign=sign*-1
    pi=pi*4
    return pi

pil=myPi(10000)
print(pil)