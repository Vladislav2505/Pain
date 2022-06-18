# В матрице элементы последнего столбца заменить на -1.

from random import randint

row = int(input())

matrix = [[randint(-2, 20) for i in range(3)] for j in range(row)]

print("Исходная матрица: ", matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j == len(matrix[i]) - 1:
            matrix[i][j] = -1

print(matrix)