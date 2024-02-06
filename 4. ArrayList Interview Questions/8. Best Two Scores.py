def first_second(my_list):
    #my_list.sort(reverse=True)
    #return my_list[0],my_list[1]
    max1, max2 = float('-inf'), float('-inf')
    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    print(max1, max2)

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList)    