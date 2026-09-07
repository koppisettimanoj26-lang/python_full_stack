'''

1. Reversing a string..and palindrome
A: Method 1:
words = 'madam'
empty_str = ''
for i in words:
    empty_str = i+empty_str
if empty_str == words :
    print(f'{words} is a palindrome')
else:
    print(f'{words} is not a palindrome')

Method 2:
words = 'madam'
leng = len(words)
print(leng)
a = leng-1
empty_str = ''
for i in range(a, -1, -1):
    empty_str = words[i]+empty_str
print(empty_str)
if empty_str == words :
    print(f'{words} is a palindrome')
else:
    print(f'{words} is not a palindrome')

2. Check num is amstrong or not
A:
num = int(input('enter a number:'))
length = len(str(num))
amstrong = 0
for i in str(num):
    print(i)
    amstrong = amstrong + int(i)**length
    print(amstrong)
if amstrong == num:
    print(f'{num} is a arstrong number')
else:
    print(f'{num} is a amstrong number')

3. check num is a perfect number
A:
num = int(input('enter any number'))
sums = 0
for i in range(1,num):
    if num%i == 0:
        sums = sums+i
if(num == sums):
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')



a, b = 0,1
user = int(input('enter number'))
print(a,b, end = ' ')
sums = 0
for i in range(1,user):
    sums = a+b
    a = b
    b = sums
    print(sums, end = ' ')

'''
words = 'rdx'
leng = len(words)
print(leng)
a = leng-1
empty_str = ''
for i in range(a, -1, -1):
    empty_str = words[i]+empty_str
print(empty_str)
if empty_str == words :
    print(f'{words} is a palindrome')
else:
    print(f'{words} is not a palindrome')
