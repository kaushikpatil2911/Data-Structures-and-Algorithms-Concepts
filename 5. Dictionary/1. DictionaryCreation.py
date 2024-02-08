my_dict = dict()
print(my_dict)
my_dict2 = {}
print(my_dict2)

# Time Complexity -> O(1)
# Space Complexity -> O(1)

# eng_sp = dict(one='uno',two='dos',three='tres')
eng_sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng_sp)

# Time Complexity -> O(N)
# Space Complexity -> O(N)

eng_sp2 = [('one','uno'),('two','dos'),('three','tres')]
eng_sp3 = dict(eng_sp2)
print(eng_sp3)