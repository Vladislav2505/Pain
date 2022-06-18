# В матрице элементы второго столбца заменить элементами из одномерного массива соответствующей размерности.

from random import randint

row = int(input())
matrix1 = [[randint(0, 10) for i in range(3)] for j in range(row)]

array = [randint(1, 5) for q in range(row)]

print(matrix1)
print(array)

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        if j == 1:
            matrix1[i][j] = array[i]

print(matrix1)
