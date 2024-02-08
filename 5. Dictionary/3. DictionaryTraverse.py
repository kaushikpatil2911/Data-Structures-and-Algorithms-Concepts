my_dict = {'name': 'Edy', 'age': 27, 'address': 'Austin'}

def traverseDict(dict):
    for key in dict:
        print(key)
        print(dict[key])

traverseDict(my_dict)

# Time Complexity -> O(N)
# Space Complexity -> O(1)