import datetime

def addlog(data):
    dt_now = str(datetime.datetime.now())
    with open('log.txt', 'a', encoding="utf-8") as file:
        file.write(dt_now + ' ' + data + '\n')
  
def read_log():
    with open('log.txt', 'r', encoding="utf-8") as file:
        for line in file:
            print(line) 
