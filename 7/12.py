#12-1
def zad121(z):
    for i in range(z, 1, -1): #перебираем все числа меньше n
        k = 0
        n = 0
        for x in range(1, i): #ищем делители и их сумму 1-го числа
            if i % x == 0:
                k += x
        for j in range(1, k): #ищем делители и их сумму 2-го числа
            if k % j == 0:
                n += j
        if i == n and i != k and i == min(i, k): #сравниваем числа
            print(i, k)


zad121(10000)


#12-2
def med(m, n, k): #объявляем процедуру
    global a, b, c
    a = (2 * (n ** 2 + k ** 2) - m ** 2) ** 0.5 / 2 #поиск медиан
    b = (2 * (m ** 2 + k ** 2) - n ** 2) ** 0.5 / 2
    c = (2 * (m ** 2 + n ** 2) - k ** 2) ** 0.5 / 2


a, b, c = map(float, input().split()) #проверка существует ли такой треугольник вообще
if a < b + c and b < a + c and c < a + b:
    med(a, b, c)
    med(a, b, c)
    print(round(a, 2), round(b, 2), round(c, 2))
else:
    print('треугольник с такими сторонами не существует')


