#8.1
from random import randint
size = int(input("Введите размер матрицы: "))
min_ = 1
max_ = 9
k = int(input("Введите номер строки: "))
mat = []
print("Начальная матрица:")
for i in range(size):
    b = []
    for j in range(size):
        b.append(int(randint(min_, max_)))
        print(b[j], end=' ')
    mat.append(b)
    print()


def funcm(mat, k):
    dg = mat[k-1][k-1]
    for j in range(len(mat[k-1])):
        mat[k-1][j] /= dg
    return mat

print("Новая матрица:")
i = funcm(mat, k)
for i in range(size):
    for j in range(size):
        print(mat[i][j], end=' ')
    print()

#8.2
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in m:
    print(i)
print()
n = 3
tm = []
for i in range(n):
    tm.append([0] * n)
for i in range(n):
    for j in range(n):
        tm[j][i] = m[i][j]
for i in range(len(tm)):
    print(tm[i])