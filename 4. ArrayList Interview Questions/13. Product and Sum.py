def prodSum(arr):
    summ = 0
    prod = 1

    for i in arr:
        summ = summ +i
        prod = prod*i

    print("Sum : "+str(summ)+ " , Product : "+str(prod))

prodSum([1,2,3,4,5])    