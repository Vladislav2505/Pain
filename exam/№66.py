# В матрице найти сумму и произведение элементов столбца N (N задать
# с клавиатуры).

from random import randint


def Foo(a, b):
    sum_el = 0
    pr_el = 1
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j == b - 1:
                sum_el += a[i][j]
                pr_el *= a[i][j]
    print(sum_el, pr_el)


row = int(input())
N = int(input())

matrix = [[randint(0, 10) for i in range(3)] for j in range(row)]

print(matrix)

if N <= 3 and N > 0:
    Foo(matrix, N)
