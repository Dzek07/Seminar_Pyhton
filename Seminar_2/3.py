str1=input("Введите первую строку: ")
str2=input("Введите вторую строку: ")
count=0
while str2 in str1:
    count+=1
    str1=str1.replace(str2, " ", 1)  
print("Колличество вхождений второй строки в первую: ", count)