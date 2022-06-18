# В матрице элементы последней строки заменить на 0

from random import randint

row = int(input())

matrix = [[randint(0, 100) for i in range(3)] for j in range(row)]

print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == len(matrix) - 1:
            matrix[i][j] = 0

print(matrix)
