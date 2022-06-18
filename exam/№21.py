# В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).

from random import randint

row = int(input())
N = int(input())
summ = 0
com = 1

matrix = [[randint(0, 100) for i in range(3)] for j in range(row)]

if N <= row and N > 0:
    print(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == N - 1:
                summ += matrix[i][j]
                com *= matrix[i][j]

    print(summ)
    print(com)
else:
    print("Ты попуск")
