myList = [1,2,3,4,5,6,7]
print(myList)

print(myList[0:2])
print(myList[:2])
print(myList[1:])
print(myList[:])

myList = [1,2,3,4,5,6,7]
myList[0:2] = ['x','y']
print(myList)

myList = [1,2,3,4,5,6,7]
myList.pop(1) # Time Complexity -> O(n) # Space Complexity -> O(1)
print(myList)

myList = [1,2,3,4,5,6,7]
myList.pop() # Time Complexity -> O(1) # Space Complexity -> O(1)
print(myList)

myList = [1,2,3,4,5,6,7]
del myList[1] # Time Complexity -> O(n) # Space Complexity -> O(1)
print(myList)

myList = [1,2,3,4,5,6,7]
del myList[0:2]
print(myList)

myList = [1,2,3,4,5,6,7]
del myList[2:4]
print(myList)

myList = [1,2,3,4,5,6,7]
myList.remove(3) # Time Complexity -> O(n) # Space Complexity -> O(1)
print(myList)