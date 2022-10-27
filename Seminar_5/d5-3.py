n = input("Введите предложение: ")
slovo = input("Введите слово или часть слова: ")


n_sp = n.split()
i=0
while i in range(len(n_sp)):
    count=0
    element = n_sp[i]
    
    while slovo in element:
        count+=1
        element=element.replace(slovo, " ", 1)
    
    if count>0:
        n_sp.pop(i)
    i+=1

print(" ".join(n_sp))