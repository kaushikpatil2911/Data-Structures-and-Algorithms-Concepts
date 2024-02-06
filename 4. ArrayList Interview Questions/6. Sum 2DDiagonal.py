import numpy as np

def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    print(sum)    

matrix = [[1,2,3],[4,5,6],[7,8,9]] 
 
diagonal_sum(matrix)