def permutation(list1, list2):
    if len(list1) != len(list2):
        print("Not a Permutation")
    list1.sort()
    list2.sort()
    if list1 == list2:
        print("Permutation")
    else:
        print("Not a Permutation")

permutation([1,2,3],[3,2,1])   
permutation(['a','b','c'],['b','a','d'])          