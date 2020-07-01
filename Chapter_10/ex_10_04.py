'''Create a list containing 100 random integers between 0 and 1000 (use iteration, append, and the random 
module). Write a function called average that will take the list as a parameter and return the average.'''

import random

rlist = []

for i in range(101):
    rlist.append(random.randrange(1,1000))

def average(list):
    avg = sum(rlist)/len(rlist)
    return avg

print(average(rlist))