import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)

new_twoDArray = np.delete(twoDArray,0,axis=0)
print(new_twoDArray)

new_twoDArray = np.delete(twoDArray,2,axis=1)
print(new_twoDArray)

# Time Complexity -> O(MN)
# Space Complexity -> O(MN)