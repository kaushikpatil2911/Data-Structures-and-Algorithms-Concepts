def sum_product(input_tuple):
    summ = 0
    prod = 1
    for i in input_tuple:
        summ = summ + i
        prod = prod * i
    print(summ,prod)

input_tuple = (1, 2, 3, 4)
sum_product(input_tuple) 