import array
import numpy as np

my_array = array.array('i',[1,2,3,4,5])
print(my_array)

np_array = np.array([], dtype=int)
print(np_array)
np_array1 = np.array([1,2,3,4])
print(np_array1)

# Time Complexity -> O(1)
# Space Complexity -> O(1)