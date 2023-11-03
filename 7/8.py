#8-1
def func1(i):
    a = i
    while(a):
        b = a % 10
        a //= 10
        if (b == 0 or i % b):
            return False
    return True
n = int(input("Введите число: "))
for i in range(1, n + 1):
    if (func1(i)):
        print(i)

#8-2
def func2(A):
    A[0], A[-1] = A[-1], A[0]
    return A

x = int(input("m = "))
A = list(map(int, input("Введите элементы массива: ").split(maxsplit = x)))
print(A)
print(func2(A))
