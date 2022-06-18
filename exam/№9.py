# В матрице элементы второго столбца возвести в квадрат

from random import randint

row = int(input())

matrix = [[randint(-2, 20) for i in range(3)] for j in range(row)]

print("Исходная матрица: ", matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j == 1:
            matrix[i][j] *= 2


print(matrix)