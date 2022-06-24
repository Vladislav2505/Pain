# Перенести в новую матрицу Matr1 элементы, которые не находятся в
# первых и последних сроках и столбцах матрицы Matr2 произвольного
# размера.

from random import randint

row = int(input())

matrix2 = [[randint(0, 10) for i in range(3)] for j in range(row)]
matrix1 = list()

print(matrix2)

for i in range(len(matrix2)):
    if i != 0 and i != len(matrix2) - 1:
        for j in range(len(matrix2[i])):
            if j != 0 and j != len(matrix2[i]) - 1:
                matrix1.append(matrix2[i][j])

print(matrix1)

