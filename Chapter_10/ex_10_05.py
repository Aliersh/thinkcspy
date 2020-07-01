'''Write a Python function that will take a the list of 100 random integers between 0 and 1000 and return 
the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)'''

import random

rlist = []

for i in range(101):
    rlist.append(random.randrange(1,1000))

def max_val(rlist):
    max = 0
    for item in rlist:
        if item > max:
            max = item
    return max

print(max_val(rlist))