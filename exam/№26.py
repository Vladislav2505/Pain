# В матрице найти максимальный положительный элемент, кратный 4.

from random import randint

row = int(input())
max = 0

matrix = [[randint(-2, 20) for i in range(3)] for j in range(row)]

print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > max and matrix[i][j] % 4 == 0 and matrix[i][j] > 0:
            max = matrix[i][j]

print(max)
