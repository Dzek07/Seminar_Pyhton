def decomposition(a,b,c):
    z=0
    j = 0
    for i in range(len(a)):
        if a[i].isdigit() == True and z == 0:
            b.append(a[i])        
            z = z + 1
        elif a[i].isdigit() == True:
            b[j] = b[j] + a[i]
        
        else: 
            z = 0
            c.append(a[i])
            if a[i-1].isdigit() == True:
                j = j + 1
def calculation(b,c):
    i=0
    j=0
    while True:
        if i>=len(c):
            j=1
            i=0
        if len(b) == 1:
            break
        if j==0:
            if c[i] == '*':
                b[i] = int(b[i]) * int(b[i+1])
                b.pop(i+1)
                c.pop(i)
            elif c[i] == '/':
                b[i] = int(b[i]) / int(b[i+1])
                b.pop(i+1)
                c.pop(i)
            else:
                i=i+1
        else:
            if c[i] == '+':
                b[i] = int(b[i]) + int(b[i+1])
                b.pop(i+1)
                c.pop(i)
            else:
                b[i] = int(b[i]) - int(b[i+1])
                b.pop(i+1)
                c.pop(i)
def bracket_search(b,c,tmp_b,tmp_c,k):
    i = 0
    while i<len(c):
        if c[i] == '(':
            tmp_b.append(b[i])
            c.pop(i)
            b[i] = 'temp'
            k = i
            while i<len(c):
                if c[i] == ')':
                    c.pop(i)
                    return k
                else:
                    tmp_b.append(b[i+1])
                    b.pop(i+1)
                    tmp_c.append(c[i])
                    c.pop(i)
                    
        i = i + 1



n = input("Введите вырожение: ")
a = list(n.strip())
b = []
c = []
tmp_b = []
tmp_c = []
k=0
decomposition(a,b,c)
k= bracket_search(b,c,tmp_b,tmp_c,k)
if len(tmp_c) > 0:
    calculation(tmp_b,tmp_c)
    b[k] = tmp_b[0]
calculation(b,c)
print("Решение = ", b[0])