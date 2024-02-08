my_dict = {'name': 'Edy','age': 27,'address': 'Austin','education':'masters'}

my_dict.clear()
print(my_dict)

my_dict = {'name': 'Edy','age': 27,'address': 'Austin','education':'masters'}
new_dict = my_dict.copy()
print(my_dict)
print(new_dict)

newDict = {}.fromkeys([1,2,3],0)
print(newDict)
newDict = {}.fromkeys([1,2,3])
print(newDict)

myDict = {'name': 'Edy','age': 27,'address': 'Austin','education':'masters'}
print(myDict.get('age'))

print(myDict.items()) #Return tuple

print(myDict.keys())
print(myDict.values())

myDict = {'name': 'Edy','age': 27,'address': 'Austin','education':'masters'}
print(myDict.popitem())
print(myDict)

myDict = {'name': 'Edy','age': 27,'address': 'Austin','education':'masters'}
print(myDict.setdefault('name','added'))
print(myDict)
print(myDict.setdefault('name1','added'))
print(myDict)

myDict = {'name': 'Edy','age': 27,'address': 'Austin','education':'masters'}
print(myDict.pop('address'))
print(myDict)

eng_sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
myDict = {'name': 'Edy','age': 27,'address': 'Austin','education':'masters'}
myDict.update(eng_sp)
print(myDict)

