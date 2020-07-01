'''Although Python provides us with many list methods, it is good practice and very instructive to think 
about how they are implemented. Implement a Python function that works like the following:
count
in
reverse
index
insert'''

def count(obj,lst):
    count = 0
    for item in lst:
        if item == obj:
            count += 1
    return count

def is_in(obj,lst):
    for item in lst:
        if item == obj:
            return True        
    return False

def reverse(lst):
    rlist = []
    pos = -1
    for item in lst:
        rlist[pos] = item
        pos -= 1
    return rlist

def index(obj,lst):
    for i in range(len(lst)):
        if lst[i] == obj:
            return i
    return -1

def insert(obj, index, lst):
    newlst = []
    for i in range(len(lst)):
        if i == index:
            newlst.append(obj)
        newlst.append(lst[i])
    return newlst