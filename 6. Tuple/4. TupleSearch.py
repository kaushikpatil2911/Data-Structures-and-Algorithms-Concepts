newTuple = ('a','b','c','d','e')
for i in newTuple:
    if i == 'a':
        print(True)
    else:
        continue    

print(newTuple.index('c'))

def searchTuple(newTuple,element):
    for i in range(len(newTuple)):
        if newTuple[i] == element:
            print(f"The element is located at {i} index")
    return False 

searchTuple(newTuple,'b')
searchTuple(newTuple,'f') 

# Time Complexity -> O(N)
# Space Complexity -> O(1)  