my_dict = {'name': 'Edy', 'age': 27, 'address': 'Austin'}

del my_dict['age']
print(my_dict)

my_dict = {'name': 'Edy', 'age': 27, 'address': 'Austin'}

new_dict = my_dict.pop('name')
print(my_dict)

my_dict = {'name': 'Edy', 'age': 27, 'address': 'Austin'}

new_dict = my_dict.pop('name')
print(my_dict)

# Time Complexity -> O(1)
# Space Complexity -> O(1)

my_dict.clear()

# Time Complexity -> O(N)
# Space Complexity -> O(1)