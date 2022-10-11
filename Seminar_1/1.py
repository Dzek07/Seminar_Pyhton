try:
    day = int(input("Введите день недели: "))
    if day > 0 and day < 6:
        print("Этот день не выходной")
    elif day > 5 and day < 8:
        print("Этот день выходной")
    else: 
        print("Вы ввели не правельное число")
except:
    print("Введены некоректные данные")