# В матрице найти сумму отрицательных элементов в первой трети матрицы.

from random import randint

row = int(input())

matrix = [[randint(-10, 10) for i in range(3)] for j in range(row)]

print(matrix)

one_third = len(matrix) // 3
print(one_third)
summ = 0

for i in range(one_third):
    for j in range(len(matrix[i])):
        if matrix[i][j] < 0:
            summ += matrix[i][j]

print(summ)
