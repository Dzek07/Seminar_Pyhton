n = int(input("Введите количество измерений от 1 до бесконечности: "))

a = []
b = []
res = []

for i in range(n):
    print("Введите а", i)
    temp = int(input())
    a.append(temp)
for i in range(n):
    print("Введите b", i)
    temp = int(input())
    b.append(temp)
for i in range(n):
    temp = (a[i] - b[i]) ** 2
    res.append(temp)

print("Расстояние = ", sum(res)**0.5)
