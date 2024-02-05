myList = [1,2,3,4,5,6,7]

target = 5

if target in myList:
    print(f"The target {target} is in the List")
else:
    print(f"The {target} is in the List")

# Time Complexity -> O(n) # Space Complexity -> O(1)

# Linear Search # Time Complexity -> O(n) # Space Complexity -> O(1)
def linearSearch(myList, myTarget):
    for i, value in enumerate(myList):
        if value == myTarget:
            return i
    return -1

print(linearSearch(myList,target))            