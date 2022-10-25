n =  int(input("Введите число: "))
i = 2
while i <= n:
    if (n % i) == 0:
        n = n / i
        if n == 1:
            print(i, end='')
        else: print(i, end=' * ')
        i = 2
    else: i = i + 1

