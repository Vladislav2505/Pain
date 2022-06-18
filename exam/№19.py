# В матрице элементы третьей строки заменить элементами из одномерного массива соответствующей размерности.

from random import randint

row = int(input())

matrix = [[randint(0, 100) for i in range(3)] for j in range(row)]
arr = [1, 2, 3]

print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == 2:
            matrix[i][j] = arr[j]

print(matrix)