from random import randint

def peremesh(a,iter):
    l = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            temp = a[i][j]
            a[i][j] = a[(i+1)*-1][(j+1)*-1]
            a[(i+1)*-1][(j+1)*-1] = temp
            l = l+1
            if l == iter:
                return




print("Введите количество строи и столбцов чтобы количество элементов было четное")
Stroka = int(input("Введите количество строк: "))
Stolbec = int(input("Введите количество столбцов: "))
iter = (Stroka*Stolbec)/2

if (Stroka*Stolbec)%2 == 0:
    a = [[randint(10, 99) for _ in range(Stolbec)] for _ in range(Stroka)]
    for row in a:
        print('|'.join([str(elem) for elem in row]))
    peremesh(a,iter)
    print('--------------------------')
    for row in a:
        print('|'.join([str(elem) for elem in row]))
else: print("Количество элементов не четное. Введите еще раз")