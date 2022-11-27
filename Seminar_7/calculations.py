import logging

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





def calc(user_expression):
    a = list(user_expression.strip())
    b = []
    c = []
    decomposition(a,b,c)
    calculation(b,c)
    result_log = "Результат: " + str(b[0])
    logging.addlog(result_log)
    return b[0]

def calc_compl(data):
    res = eval(data)
    result_log = "Результат: " + str(res)
    logging.addlog(result_log)
    return res




