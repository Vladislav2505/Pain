# В матрице элементы строки N (N задать с клавиатуры) увеличить на 3

from random import randint

matrix = [[randint(0, 10) for i in range(3)] for j in range(5)]
N = int(input("Введите строку: "))

if N <= 5 and N > 0:

    print(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == N - 1:
                matrix[i][j] += 3

    print(matrix)

else:
    print("Такой строки нет")
