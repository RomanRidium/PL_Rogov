# 7
a = input("Введите строку: ")
n = len(a)
n2 = n//2
b = a[:n2]+a[n2:].replace('п', '*')
print("Преобразованная строка:", b, n)