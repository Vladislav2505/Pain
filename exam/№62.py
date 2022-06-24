# В матрице элементы второго столбца заменить элементами из
# одномерного массива соответствующей размерности.

from random import randint

row = int(input())
column = int(input())

if column >= 2:
    matrix = [[randint(-2, 20) for i in range(column)] for j in range(row)]
    new_Array = [randint(0, 10) for q in range(row)]

    print("Исходная матрица: ", matrix)
    print("Одномерный массив: ", new_Array)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == 1:
                matrix[i][j] = new_Array[i]

    print(matrix)

else:
    print("NO")