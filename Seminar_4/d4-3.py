from random import randint

k = int(input("Введите натуральную степень k: "))
i = k
res = ''
while i > -1:
    if (i == k):
        a = randint(1, 100)
        if a == 1:
           res = 'x^' + str(i) 
        res = str(a) + '*x^' + str(i)
    elif i > 1:
        a = randint(0, 100)
        if a == 1:
            res = res + ' + x^' + str(i)
        elif a > 1:
            res = res + ' + ' + str(a) + '*x^' + str(i)
    elif i == 1:
        a = randint(0, 100)
        if a > 1:
            res = res + ' + ' + str(a) + '*x'
        elif a == 1:
            res = res + ' + x'
    else:
        a = randint(0, 100)
        if a > 1:
            res = res + ' + ' + str(a) + ' = 0'
        else: res = res + ' = 0'
    i = i - 1

data = open('text.txt', 'a')
data.write(res + '\n')
data.close()


print(res)