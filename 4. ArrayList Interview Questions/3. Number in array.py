import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10,3])

def findNumber(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            print("Number present at position "+str(i))  

findNumber(myArray,3)            