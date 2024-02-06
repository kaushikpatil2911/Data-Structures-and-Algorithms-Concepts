def reverse(arr):
    for i in range(int(len(arr)/2)):
        other = len(arr)-i-1
        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp
    print(arr)

reverse([1,2,3,4])        