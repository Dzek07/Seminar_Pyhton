x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))


a = not (x or y or z) 
b = not x and not y and not z
if a == b:
    print("Вырожение верно")
else:
    print("Вырожение не верно")