my_dict = {'name': 'Edy', 'age': 27, 'address': 'Austin'}

def searchDict(dict,value):
    for key in dict:
        if dict[key] == value:
            print(key,value)

searchDict(my_dict,27)
searchDict(my_dict,28)

# Time Complexity -> O(N)
# Space Complexity -> O(1)