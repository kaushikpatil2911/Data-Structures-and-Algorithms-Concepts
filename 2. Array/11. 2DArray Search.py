import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)

def search2DArray(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                print(f"The element {target} is found in position "+str(i)+" "+str(j))
    return 'Element not found!!!'

search2DArray(twoDArray,11)
search2DArray(twoDArray,6)
search2DArray(twoDArray,13)

# Time Complexity -> O(MN)
# Space Complexity -> O(1)