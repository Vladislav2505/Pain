# Сгенерировать матрицу на произвольное количество элементов, в
# которой задается преобразование от предыдущего элемента к
# следующему на произвольное значение.

N = int(input())
P = N
matrix = [[0 for i in range(3)] for j in range(3)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = matrix[i][j] + P
        P += N

print(matrix)
