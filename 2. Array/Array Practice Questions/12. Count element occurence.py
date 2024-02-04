from array import *

my_array = array("i",[1,2,3,4,5,3,4,5,5,3,4,2,3,1])

x = int(input("Enter the number : "))
count = my_array.count(x)
print(f"Number of occurences for {x} : {count}")