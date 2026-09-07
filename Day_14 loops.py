'''
1.Check wheather the given number is odd or even

A:
ran = int(input('enter any num'))
for i in range(1, ran+1):
    if i%2 != 0:
        print(f'{i} is a odd number')

---------------------------------------------------------------------

2. To get the value present in the nums..

A:
nums = [23,78,97,5]
for i in (nums):
    print(i)

----------------------------------------------------------------------

3. Check the number of vowels in given words?

A:
words_ = input('enter a word: ').lower()
vowels = 'aeiou'
count = 0
for i in words_:
    if i in vowels:
        count += 1
        print(f'{i} is vowel')
print(count)

------------------------------------------------------------------------

4. Remove dulipicate from the list?

A:
digits = [1,2,3,1,5,2]
empty =[]
for i in digits :
    if i not in empty:
        empty.append(i)
print(empty)

5. Find the duplicate from tuple
A: method1 :

digits = (1,3,2,3,2,1)
emp = []
for i in digits:
    if i not in emp:
        emp.append(i)
print(tuple(emp))

method 2:

digits = (1,3,2,3,2,1)
emp = ()
for i in digits:
    if i not in emp:
        emp += (i,)
print(emp)

6. Print the number of words in the string..
A : using built in functions
-------------------------------------
words_ = 'python is a language'
cou_ =  words_.split(' ')
print(len(cou_))

without using bulit-in
--------------------------------------
text = 'python is a la nguage'
count = 0

for i in range(len(text)):
    if text[i] == ' ':
        count += 1

print(count+1)
-------------------------------------------------------------------------

'''
