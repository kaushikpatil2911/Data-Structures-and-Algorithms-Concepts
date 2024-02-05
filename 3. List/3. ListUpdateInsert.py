myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33
print(myList)

myList = [1,2,3,4,5,6,7]

#Insert at begin # Time Complexity -> O(n) # Space Complexity -> O(1)
myList.insert(0,11)
print(myList)

#Insert in any place # Time Complexity -> O(n) # Space Complexity -> O(1)
myList.insert(4,44)
print(myList)

#Insert at end # Time Complexity -> O(1) # Space Complexity -> O(1)
myList.append(88)
print(myList)

newList = [10,20,30,40,50] 
#Insert nother list to list # Time Complexity -> O(n) # Space Complexity -> O(n)
myList.extend(newList)
print(myList)