from decimal import Decimal
a = [Decimal('1.1'), Decimal('1.2'), Decimal('3.1'), Decimal('5'), Decimal('10.01')]

for i in range(len(a)):
    a[i] = a[i] - int(a[i])
min = a[0]
max = a[0]
for i in range(len(a)):
    if (min > a[i]) and (a[i] != 0):
        min = a[i]
    elif max < a[i]:
        max = a[i]

res = max - min
print(res)