# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.

from random import randint

matrix = [[randint(1, 10) for i in range(3)] for j in range(3)]
print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j == i:
            continue
        else:
            matrix[i][j] *= 2


print(matrix)
