# Из матрицы сформировать массив из положительных четных элементов,найти их сумму и среднее
# арифметическое.

from random import randint

row = int(input())

matrix = [[randint(-2, 10) for i in range(3)] for j in range(row)]

print("Исходная матрица: ", matrix)

my_array = list()
arr_summ = float(0)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 == 0 and matrix[i][j] > 0:
            my_array.append(matrix[i][j])

for i in range(len(my_array)):
    arr_summ += my_array[i]

print("Массив пол четных элементов: ", my_array)
print("Сумма массива: ", arr_summ)
print("Среднее арифметическое: ", arr_summ // len(my_array))
