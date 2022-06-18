# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.

from random import randint

row = int(input())

matrix = [[randint(-2, 20) for i in range(3)] for j in range(row)]
truth = True

print("Исходная матрица: ", matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < 0:
            truth = False
            break

print(truth)
