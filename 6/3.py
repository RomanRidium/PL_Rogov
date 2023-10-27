s = [1, 2, 3, 4, 5]
summ = 0 
for i in range(len(s)):
    if i%2==0:
       summ+=s[i]
print(s, summ)

s = [1, 2, 3, 4, 5, 6, 17, 16]
for i in range(len(s)):
    if s[i] < 15: 
        s[i] = s[i]*2 
print(s)
