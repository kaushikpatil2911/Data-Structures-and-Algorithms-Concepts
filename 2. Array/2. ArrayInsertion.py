import array
import numpy as np

my_array = array.array('i',[1,2,3,4])
print(my_array)
my_array.insert(0,6)
print(my_array)

my_array1 = np.asarray([1,2,3,4,5])
print(my_array1)
my_array2 = np.insert(my_array1,0,6)
print(my_array2)
# NumPy insert() doesn't modify the original array. Hence, it returns a copy of the original collection, with the values positioned according to the parameters.

# Time Complexity -> O(N)
# Space Complexity -> O(1)