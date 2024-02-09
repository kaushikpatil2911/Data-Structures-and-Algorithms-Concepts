def check_same_frequency(list1, list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        print(True)
    else:
        print(False)    

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 2]
check_same_frequency(list1, list2)