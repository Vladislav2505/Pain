# В матрице найти суммы элементов каждой строки и поместить их в
# новый массив. Выполнить замену элементов третьего столбца исходной
# матрицы на полученные суммы.

from random import randint

matrix = [[randint(-2, 20) for i in range(3)] for j in range(3)]
newarr = [0 for q in range(3)]

print(matrix)

for i in range(len(matrix)):
    newarr[i] = sum(matrix[i])

print(newarr)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j == 2:
            matrix[i][j] = newarr[i]

print(matrix)