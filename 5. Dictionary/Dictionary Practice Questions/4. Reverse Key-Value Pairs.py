def reverse_dict(my_dict):
    print({v: k for k, v in my_dict.items()})

my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)