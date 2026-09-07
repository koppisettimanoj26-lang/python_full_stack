'''
1. Print the number in loop until the limit
A: limit_ = 10
for i in range(1,limit_+1):
    for j in range(1,i+1):
        print(j)

2. Print the prime numbers in the given range
A: 
limit_ = 10
    for i in range(1,limit_+1):
        count = 0
        for j in range(1,i+1):
            if i%j == 0 :
                count +=1
        if count == 2:
            print(f'{i} is prime')
    

user input :
-------------
limit_ = int(input())
for i in range(1,limit_+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0 :
            count +=1
    if count == 2:
        print(f'{i} is prime')

3. Print triangle pattern using * ?
A:
for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()
o/p:
* 
* * 
* * * 
* * * * 
* * * * * 


4. print triangle pattern using number?
A:
for i in range(5):
    for j in range(i+1):
        print(j,end=' ')
    print()
o/p:
0 
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4

5. print triangle pattern using number value should not repeat?

A:
count = 0
for i in range(5):
    for j in range(i+1):
        count += 1
        print(count,end=' ')
    print()
o/p:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15


6. Inverted triangle
A: using while loop
i = 5
while(i>=1):
    j = 1
    while(j<=i):
        print('*', end= ' ')
        j += 1
    print()
    i -= 1

using for loop

i = 5
for i in range (5,0,-1):
    j = 1
    for j in range (1,i+1):
         print('*', end= ' ')
    print()
'''


for i in range (5,0,-1):
    j = 1
    for j in range (1,i+1):
         print('*', end= ' ')
    print()
        
