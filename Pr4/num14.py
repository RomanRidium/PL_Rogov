#14
print("Введите координаты точки")
x = int(input())
y = int(input())
for a in range(1, 6):
    for b in range(1, 6):
        if x == a and y == b:
            print("Координаты подходят!")
            exit()
        else:
            print("Координаты не подходят!")
            exit()