# Для каждой строки матрицы с нечетным номером найти среднее
# арифметическое ее элементов.

from random import randint

row = int(input())

matrix = [[randint(-10, 10) for i in range(3)] for j in range(row)]

print(matrix)

for i in range(len(matrix)):
    if i % 2 != 0:
        print("Среднее ариф", i, "строки", sum(matrix[i]) // len(matrix[i]))
