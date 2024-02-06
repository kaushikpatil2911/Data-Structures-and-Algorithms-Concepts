def missing_number(arr, n):
    total = (n * (n + 1))/2
    sum_arr = sum(arr)
    missing = int(total - sum_arr)
    print("Missing number : "+str(missing))

missing_number([1,2,3,4,5,6,8,9,10],10)