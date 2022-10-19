n = int(input("Введите число: "))
res = ' '
while n != 0:
    t = n % 2
    n = n // 2
    res =  str(t) + str(res)

print(res)