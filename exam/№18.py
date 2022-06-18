# В матрице найти среднее арифметическое положительных элементов, кратных 3.

from random import randint

row = int(input())

matrix = [[randint(0, 100) for i in range(3)] for j in range(row)]

print(matrix)

arr = list()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 3 == 0 and matrix[i][j] > 0:
            arr.append(matrix[i][j])

print(arr)
print(sum(arr) // len(arr))