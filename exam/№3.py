# В матрице найти минимальный и максимальные элементы.

from random import randint

row = int(input("Введите кол строк: "))

matrix = [[randint(0, 100) for i in range(3)] for j in range(row)]

print("Исходная матрица: ", matrix)

max_ = matrix[0][0]
min_ = matrix[0][0]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > max_:
            max_ = matrix[i][j]
        if matrix[i][j] < min_:
            min_ = matrix[i][j]

print(max_, min_)
