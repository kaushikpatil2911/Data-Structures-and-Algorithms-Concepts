from array import *

my_array = array('i',[1,2,3,4,5])

def accessingArray(array,index):
    if index >= len(array):
        print("No element at this index")
    else:
        print(array[index])

accessingArray(my_array,2)
accessingArray(my_array,6)

# Time Complexity -> O(1)
# Space Complexity -> O(1)