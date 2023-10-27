n = int(input("Введите длину массива: ")) 
a = []
for i in range(n):
    print("Введите ", i, 'элемент')
    a.append(int(input())) 
print("Максимальный элемент списка: ", max(a))
a.reverse()
print(a) 

def zero_elemets(n):
    summ = sum(n) 
    zero_count = n.count(0)
    average = summ / len(n) 
    for i in range(len(n)): 
        if lst[i] == 0:
            lst[i] = average 
    return n

lst = [1,0,67,4,7,2,5,0,0,0,6,4,3,6,7,2,5,8,5]
print(zero_elemets(lst)) 
