# В матрице найти суммы элементов каждого столбца и поместить их в
# новый массив. Выполнить замену элементов второй строки исходной
# матрицы на полученные суммы.

from random import randint

row = int(input())

matrix = [[randint(-2, 20) for i in range(3)] for j in range(row)]
newarr = [0 for q in range(row)]

print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if j == 0:
            newarr[j] += matrix[i][j]
        elif j == 1:
            newarr[j] += matrix[i][j]
        elif j == 2:
            newarr[j] += matrix[i][j]

print(newarr)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == 1:
            matrix[i][j] = newarr[j]

print(matrix)
