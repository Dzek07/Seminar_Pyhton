try:
    x = int(input("Введите x: "))
    y = int(input("Введите y: "))

    if x > 0 and y > 0:
        print("x=", x, "y=", y, "-> 1-я координатная четверть")
    elif x < 0 and y > 0:
        print("x=", x, "y=", y, "-> 2-я координатная четверть")
    elif x < 0 and y < 0:
        print("x=", x, "y=", y, "-> 3-я координатная четверть")
    elif x > 0 and y < 0:
        print("x=", x, "y=", y, "-> 4-я координатная четверть")
    else:
        print("Вы ввели не коректное значение, введите координаты заново без 0")
except:
    print("Введены некоректные данные")