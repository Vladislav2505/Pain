from random import randint

matrix = [[randint(0, 5) for i in range(3)] for j in range(6)]

print(matrix)

p = len(matrix) // 2
summ = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i >= p:
            summ += matrix[i][j]

print(summ)