from array import *

my_array = array("i",[1,2,3,4,5])
my_array2 = array("i",[10,20,30,40,50])

my_array.extend(my_array2)
print(my_array)
print(my_array2)