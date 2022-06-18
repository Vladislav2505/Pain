# Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.

from random import randint

row = int(input())

matrix = [[randint(0, 10) for i in range(3)] for j in range(row)]

print("Исходная матрица: ", matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 != 0:
            matrix[i][j] = 0


print(matrix)