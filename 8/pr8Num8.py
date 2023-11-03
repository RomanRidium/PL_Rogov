#8.1
from random import randint
size = int(input("Введите размер матрицы: ")) #Количество цифр в строках и столбцах
min = 1 #Минимальное числовое значение
max = 9 #Максимальное числовое значение
k = int(input("Введите номер строки: "))
A = [] #Пустой список, в который будут генерироваться значения
print("Начальная матрица:")
for i in range(size): #Матрица начальная
    b = []
    for j in range(size):
        b.append(int(randint(min, max))) #добавление в конец списка случайное число
        print(b[j], end=' ') #Вывод с отступом в end
    A.append(b)
    print()

def funcm(A, k): #Функция делящая каждый элемент строки на диагональный элемент
    dg = A[k-1][k-1]
    for j in range(len(A[k-1])):
        A[k-1][j] /= dg
    return A

print("Изменённая матрица:")
i = funcm(A, k)
for i in range(size): #Цикл выводящий изменённую матрицу
    for j in range(size):
        print(A[i][j], end=' ')
    print()

#8.2
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in m:
    print(i)
print()
n = 3
tm = [] #Пустой список
for i in range(n):
    tm.append([0] * n) #добавление в пустой список и создание таблицы с длинной n
for i in range(n):
    for j in range(n):
        tm[j][i] = m[i][j] #Замена чисел местами по индексу
for i in range(len(tm)):
    print(tm[i])