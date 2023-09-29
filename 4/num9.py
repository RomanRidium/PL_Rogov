#9
def sum_fib(n, s=0, c=0, p=1):
    if n == 0:
        return s
    return sum_fib(n - 1, s + c + p, c + p, c)


n = int(input())
print(sum_fib(n))