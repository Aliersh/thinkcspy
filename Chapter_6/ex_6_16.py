'''Write a function called myPi that will return an approximation of PI (3.14159…). 
Use the Madhava approximation.'''

import math

def myPi(iters):
  sign = 1
  x = 1
  y = 0
  series = 0 
  for i in range (iters):
    series = series + (sign/(x * 3**y))
    x = x + 2
    y = y + 1
    sign = sign * -1
  myPi = math.sqrt(12) * series

  return myPi

print(myPi(1000))