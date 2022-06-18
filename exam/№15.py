# В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.

from random import randint

row = int(input())
column = int(input())
N = int(input())

matrix = [[randint(0, 10) for i in range(column)] for j in range(row)]

if N <= column and N > 0:
    print(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == N - 1:
                matrix[i][j] *= 2

    print(matrix)

else:
    print("Нет такого столбца")
