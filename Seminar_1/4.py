#Поддерживаемые операции: +, -, /, *, mod, pow, div, где
#mod — это взятие остатка от деления,
#pow — возведение в степень,
#div — целочисленное деление.

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    option = input("Введите операцию: ")

    if option == "+":
        res = num1 + num2
        print("Ответ = ", res)
    elif option == "-":
        res = num1 - num2
        print("Ответ = ", res)
    elif option == "*":
        res = num1 * num2
        print("Ответ = ", res)
    elif option == "/":
        if num2 == 0:
            print("Делить на 0 НЕЛЬЗЯ")
        else:
            res = num1 / num2
            print("Ответ = ", res)
    elif option == "mod":
        if num2 == 0:
            print("Делить на 0 НЕЛЬЗЯ")
        else:
            res = num1 % num2
            print("Ответ = ", res)
    elif option == "pow":
        res = num1 ** num2
        print("Ответ = ", res)
    elif option == "div":
        if num2 == 0:
            print("Делить на 0 НЕЛЬЗЯ")
        else:
            res = num1 // num2
            print("Ответ = ", res)
    else:
        print("Введены некоректные данные")
except:
    print("Введены некоректные данные")