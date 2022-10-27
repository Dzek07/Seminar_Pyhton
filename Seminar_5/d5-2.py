
def coderle(s):
 
    coderle = ""
 
    i = 0
    while i < len(s):
        
        count = 1
 
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
 
        
        coderle += str(count) + s[i]
        i = i + 1
 
    return coderle
 
def undode(r):
    undode = ''
    i = 0
    while i < len(r):
        j=0
        while j<int(r[i]):
            undode = undode + r[i+1]
            j=j+1
        i = i + 2
    return undode



#Кодирование
read = open('nokod.txt','r')
upload = open('kod.txt','w')
s = read.readline()
print(coderle(s))
upload.write(coderle(s))
upload.close()

#Раскодирование
#read1 = open('kod.txt','r')
#upload1 = open('nokod1.txt','w')
#r=read1.readline()
#print(undode(r))
#upload1.write(undode(r))
#upload1.close()