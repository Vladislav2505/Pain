# В матрице отрицательные элементы возвести в квадрат.

from random import randint

row = int(input("Введите количество строк: "))

matrix1 = [[randint(-10, 10) for p in range(3)] for q in range(row)]

print("Исходная матрица: ", matrix1)

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        if matrix1[i][j] < 0:
            matrix1[i][j] = matrix1[i][j] ** 2

print(matrix1)
