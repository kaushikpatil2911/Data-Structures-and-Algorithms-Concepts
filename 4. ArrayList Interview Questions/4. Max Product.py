def max_product(arr):
    arr.sort(reverse=True)
    print(arr[0]*arr[1])

arr = [1, 7, 3, 4, 9, 5] 
max_product(arr)    

#Without Sort function
def max_product(arr):
    max1 = 0
    max2 = 0

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num    

    maxProd = max1 * max2
    print("Maximum Product : "+str(maxProd))

arr = [1, 7, 3, 4, 9, 5]
max_product(arr)         