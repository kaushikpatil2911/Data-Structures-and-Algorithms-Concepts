from array import *

my_array = array('i',[1,2,3,4,5])

def arrayLinearSearch(array,target):
    for i in range(len(array)):
        if target == array[i]:
            print(f"Array is present at position {i}")
    return -1

arrayLinearSearch(my_array,5)

# Time Complexity -> O(N)
# Space Complexity -> O(1)