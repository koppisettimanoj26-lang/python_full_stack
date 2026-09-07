'''
math
---------
import math
print(math.pi)
print(math.ceil(4.3))
print(math.floor(5.6))
print(math.sqrt(25))
print(math.sin(2))
print(math.pow(2,3))
print(math.cos(5))

random
--------
import random
print(random.randint(100000,999999))
print(random.randrange(1,100))
color = ['red','green','yellow','blue','orange']
print(random.choice(color))
random.shuffle(color)
print(color)

platform
--------
import platform
print(platform.python_version())
print(platform.system())
print(platform.platform())
print(platform.processor())

collection
--------------

import collections
data_ = ['banana','apple','banana','orange','orange']
print(collections.Counter(data_))
all_ = collections.Counter(data_)
print(all_.most_common())

from collections import defaultdict
data_ = defatdict(list)
data_['python'].append('teja')
data_['python'].append('manoj')
data_['java'].append('mmm')
print(data_)

DateTime
----------

from datetime import datetime
today = datetime.today()
print(today.month)
print(today.day)
print(today.year)
print(today.hour)
print(today.minute)

from datetime import datetime
now = datetime.now()
print(now.strftime('%d-%m-%Y'))
print(now.strftime('%H:%M:%S'))
print(now.strftime('%A'))

import random
ran = random.randrange(1,10)
attempt = 3
print(ran)
count = 0
while(attempt>0):
    user_ = int(input('enter no b/w 1 to 100'))
    count += 1
    if (ran == user_):
        print('guess is correct')
        break
    else:
        print('guess is incorrect')
        attempt -= 1
if(count == 1):
    print('prize money is 500')
elif(count == 2):
    print('prize money is 299')
elif(count == 3):
    print('prize money is 199')
else:
    print('better luck nxt time')
print(f'{ran} is the guessing number')
'''

import itertools
a = itertools.count(45)
print(next(a))
print(next(a))
b = itertools.repeat('python',6)
for j in b:
    print(j)

c = itertools.cycle(['python','java','c'])
for j in range(5):
    print(next(c))

n = itertools.chain([1,2,3],[4,5,6])
print(next(n))
