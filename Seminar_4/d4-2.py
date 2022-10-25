from random import randint

n =  int(input("Введите количество элементов: "))
a = []

for i in range(n):
    tmp = randint(0, 9)
    a.append(tmp)
print(a)
proh = len(a)
for i in range(proh):
    j = i+1
    while j < (proh):
        if a[i] == a[j]:
            a.pop(j)
            proh = proh - 1
        else: j = j +1


print(a)
