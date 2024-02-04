from array import *

my_array = [1,2,3,4,5]

my_array.insert(2,1)
print(my_array)

x = int(input("Enter the index position : "))
y = int(input("Enter the value to be inserted : "))
my_array.insert(x,y)
print(my_array)