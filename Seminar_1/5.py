from random import randint
try:
    Stroka = int(input("Введите количество строк: "))
    Ctolbec = int(input("Введите количество столбцов: "))

    a = [[randint(0, 100) for _ in range(Ctolbec)] for _ in range(Stroka)]
    for row in a:
        print(' '.join([str(elem) for elem in row]))

    for i in range(len(a)):
        for j in range(len(a[i])):
            for i1 in range(len(a)):
                for j1 in range(len(a[i1])):
                    if a[i][j] < a[i1][j1]:
                        tmp = a[i][j]
                        a[i][j] = a[i1][j1]
                        a[i1][j1] = tmp


    print("----------------------")
    for row in a:
        print(' '.join([str(elem) for elem in row]))
except:
    print("Введены некоректные данные")