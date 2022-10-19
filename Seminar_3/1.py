from random import randint

n = int(input("Введите количество элементов: "))

a = [randint(0, 20) for _ in range(n)]
print(a)

for i in range(len(a)):
    if i%2 == 0:
        a[i] = 0

print(f'Сумма элементов стоящих на нечетных позициях равна: {sum(a)}')
