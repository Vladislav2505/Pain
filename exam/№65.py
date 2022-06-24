# Из матрицы сформировать массив из положительных четных элементов,
# найти их сумму и среднее арифметическое.

from random import randint


def Foo(a):
    newArray = list()
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] % 2 == 0 and a[i][j] > 0:
                newArray.append(a[i][j])
    print(newArray)
    return sum(newArray), sum(newArray) // len(newArray)


row = int(input())

matrix = [[randint(0, 10) for i in range(3)] for j in range(row)]

print(matrix)
print(f"Сумма и среднее ариф: {Foo(matrix)}")
