# В матрице найти сумму элементов первых двух строк

from random import randint

row = int(input())

matrix = [[randint(0, 10) for i in range(3)] for j in range(row)]

print(matrix)

max_el = matrix[0][0]
min_el = matrix[0][0]


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][i] > max_el:
            max_el = matrix[i][j]
        if matrix[i][j] < min_el:
            min_el = matrix[i][j]

print(max_el)
print(min_el)
