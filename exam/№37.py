# В матрице найти среднее арифметическое элементов последних двух
# столбцов.

from random import randint

matrix = [[randint(-2, 20) for i in range(3)] for j in range(3)]
myarr = list()
print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j >= len(matrix[i]) - 2:
            myarr.append(matrix[i][j])

print(myarr)
print(sum(myarr) // len(myarr))
