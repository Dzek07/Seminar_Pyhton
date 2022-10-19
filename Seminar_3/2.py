from random import randint

n = int(input("Введите количество элементов: "))

a = [randint(0, 10) for _ in range(n)]
print(a)

b = []
j=-1
if (len(a)%2) == 0:
    k = int(len(a)/2)
else: k = round(len(a)/2)+1
for i in range(k):
    temp = a[i] * a[i+j]
    b.append(temp)
    j = j -2

print(b)
