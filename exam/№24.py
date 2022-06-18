# В матрице найти отрицательные элементы, сформировать из них новый массив. Вывести размер полученного массива.

from random import randint

row = int(input())

matrix = [[randint(-10, 10) for i in range(3)] for j in range(row)]
arr = list()

print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < 0:
            arr.append(matrix[i][j])

print(arr)
print(len(arr))
