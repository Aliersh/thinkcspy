'''Create a list called myList with the following six items: 76, 92.3, “hello”, True, 4, 76. Do it with 
both append and with concatenation, one item at a time.'''

myList = []
myList.append(76)
myList.append(92.3)
myList.append('hello')
myList.append(True)
myList.append(4)
myList.append(76)
print(myList)

cmyList = []
cmyList = cmyList + [76]
cmyList = cmyList + [92.3]
cmyList = cmyList + ['hello']
cmyList = cmyList + [True]
cmyList = cmyList + [4]
cmyList = cmyList + [76]
print(cmyList)