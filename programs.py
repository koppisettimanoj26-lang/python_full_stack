'''
# write a python program to calculate the area of the rectangle given its len and width?

length = 3
width = 5
area = length * width
print(f'{area} is the area of the rectangle')

# Create a program that takes a user's name and age as input and print a greeting message.

name = input('enter the name')
age = int(input('enter age'))
print(f'hello{name}')

# write a program to check if a number is even or odd.

num = int(input('enter a number'))
if num%2 == 0:
    print(f'{num} is even')
else :
    prinnt(f'{num} is odd')

given a list of numbers, find the maximum and min values

data_ = [22,66,44,99,3,67]
max_ = data_[0]
min_ = data_[0]

for i in data_:
    if(i>max_):
        max_ = i
    elif(i<min_):
        min_ = i
print(min_)
print(max_)

Create a function to check wheather a given string is pailnodrome or not
method-1
---------
def pal(s):
    str1 = ''
    for i in s:
        str1 = i+str1
    print(str1)
    if(str1 == s):
        return 'palindrome'
    else :
        return  'not a palindrome'
print(pal('madam'))

method-2
---------
def pal(s):
    a = len(s)
    a = a-1
    print(a)
    str1 = ''
    for i in range(a,-1,-1):
        str1 = str1+s[i]
        print(str1)
    if(str1 == s):
        return 'palindrome'
    else :
        return  'not a palindrome'
print(pal('rdx'))

method-3
--------
def pal(s):
    str1 = ''
    str2 = ''
    for i in s:
        str2 = str2+i
        print(str2)
        str1 = i+str1
        print(str1)
    if(str1 == s):
        return 'palindrome'
    else :
        return  'not a palindrome'
print(pal('rdx'))

6. calculate the compound interest for a given principle amount, interest rate, and time period

p_a = 10000
ir = 2
c = 1
t = 3
val = p_a*(1+ir/c)**t
print(val)

o/p: 27000

7. write a program to convert a given number of days into year ,months, days?

n = int(input())
years = n//365
n = n%365
month = n//30
n = n%30
days = n
print(f'{years} years {month} months {days} days')

8. given a list of integers and print the sum of all positive integers 
'''
lst = [1,5,2,4,8,6,7]
sums = 0
for i in lst:
    if(i%2==0):
        sums = sums+i
print(sums)

