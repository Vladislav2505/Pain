# Если в матрице имеются положительные элементы, то вывести TRUE,
# иначе FALSE.

from random import randint


def Foo(a):
    truth = False
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > 0:
                truth = True
                break
    print(truth)


row = int(input("Введите количество строк: "))

matrix1 = [[randint(-10, 1) for p in range(3)] for q in range(row)]

print("Исходная матрица: ", matrix1)

Foo(matrix1)
