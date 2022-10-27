from random import randint

candies = 2021
print("Всего ", candies, " конфет")
ran = randint(0, 2)

print("Осталось: ", candies, "конфет")
while True:
    if (ran % 2 == 0):
        n = int(input("Ваш ход: "))
        while True:
            if n >0 and n<29:
                if candies < 28:
                    if n > candies:
                        n = int(input("Вы ввели не корректное значение, результат получается отрицательный, введите корректное значение: "))
                    else:
                        break
                else:                
                    break
            else:
                n = int(input("Вы ввели не корректное значение, введите число от 1 до 28: "))
            
    else:
        if candies < 28:
            n = candies
        else:
            n = randint(1, 28)
        print("ИИ сделал ход: ", n)
    candies = candies - n
    print("Осталось: ", candies, "конфет")
    if candies == 0:
        if (ran % 2 == 0):
             print("Вы победили!!!!!")
             break
        else:
            print("Победил ИИ")
            break
    
    ran = ran + 1