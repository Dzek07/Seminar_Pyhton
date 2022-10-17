from decimal import Decimal

number = Decimal(input("Ввидите число: "))
integer = int(number)
fractional = Decimal(number) - int(integer)
result = 0
while integer>0:
    tmp = integer % 10
    integer = integer // 10
    result = result + tmp
tmp = 0
while fractional != 0:
    fractional = fractional * 10
    tmp = int(fractional)
    fractional = fractional - tmp
    result = result + tmp

print("Сумма чисел равна: ", result)