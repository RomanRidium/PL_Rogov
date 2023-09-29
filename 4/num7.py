#7
n = int(input())
summ = 0
previous = 1
for i in range(1, n + 1):
    current = previous * i
    summ += current
    previous = current
print(summ)