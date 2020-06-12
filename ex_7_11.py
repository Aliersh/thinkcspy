'''Extend the above program so that the sides can be given to the function in any order.'''

def is_rightangled(a,b,c):
    if c>a and c>b:
        hyp=c**2
        sd1=a**2
        sd2=b**2
        if abs(hyp-(sd1+sd2))<0.001:
            return True
        else:
                return False
    elif a>b and a>c:
        hyp=a**2
        sd1=b**2
        sd2=c**2
        if abs(hyp-(sd1+sd2))<0.001:
            return True
        else:
            return False
    elif b>a and b>c:
        hyp=b**2
        sd1=a**2
        sd2=c**2
        if abs(hyp-(sd1+sd2))<0.001:
            return True
        else:
            return False

tr=is_rightangled(4.1,8.2,9.1678787077)
print(tr)