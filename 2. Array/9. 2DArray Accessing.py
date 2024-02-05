import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])       

def accessElements(array, rowIndex, columnIndex):
    if rowIndex >= len(array) and columnIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][columnIndex])

accessElements(twoDArray,2,3)

# Time Complexity -> O(1)
# Space Complexity -> O(1)