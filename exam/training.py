# Для каждого столбца матрицы с четным номером найти сумму ее
# элементов.

from random import randint

row = int(input())
column = int(input())

matrix = [[randint(0, 100) for i in range(column)] for j in range(row)]

count = 0
print(matrix)

while count < len(matrix):
    summ = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j % 2 == 0 and j == count:
                summ += matrix[i][j]

    if count % 2 == 0:
        print(summ)
    count += 1

