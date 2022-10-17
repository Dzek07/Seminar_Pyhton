from random import randint
from datetime import datetime
import time

start_time = datetime.now()
repeat = 100
number_of_decades = randint(5, 25)

for i in range(repeat):
    for j in range(number_of_decades):
        x = randint(0, 1)
        y = randint(0, 1)
        z = randint(0, 1)
        a = not (x or y or z)
        b = not x and not y and not z
        resoult = a == b


print(datetime.now() - start_time)