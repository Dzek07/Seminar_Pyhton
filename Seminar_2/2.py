temp = 1
n = int(input("Введите число: "))
a = []
for i in range(1, n+1):
    temp = temp * i
    a.append(temp)

print(a)