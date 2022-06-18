# Перенести в новую матрицу Matr1 элементы, которые не находятся в
# первых и последних строках и столбцах матрицы Matr2 произвольного
# размера.

from random import randint

row = int(input("Введите количество строк: "))

matrix1 = [
    [23, 3, 4],
    [3, 4, 55],
    [2, 3, 2]
]

matrix2 = [[randint(0, 10) for p in range(3)] for q in range(row)]

print("Исходная матрица: ", matrix1)
print("Матрица №2: ", matrix2)

el = matrix2[1:-1]

for i in range(len(el)):
    matrix1.append(el[i][1:-1])

print("Итоговая матрица: ", matrix1)