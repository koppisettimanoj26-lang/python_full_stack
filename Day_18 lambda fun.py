'''
lambda function
--------------

--> lambda function is small anonymous function
--> lambda can take n number aruguments, but only with one expression
--> The function is defined by using lambda keyword
syntax:
---------
lambda arguments : expressions

eg:

add_ = lambda a,b,c : a+b+c
print(add_(10,20,30))

eg:60

eg: check the number greater from given numbers

grt_ = lambda a,b : a if(a>b) else b
print(grt_(14,16))

o/p : 16


eg: print the cube of the given numbers..

grt_ = lambda a : a**3
print(grt_(3))

o/p: 27

filter()
---------
--> filter() function will perform only on selected elements of iterables
syntax --> filters(lambda arguments: expression, iterable)

eg:
---
nums = [1,2,3,4,5]
data_ = list(filter(lambda a: a%2 == 0 , nums))
print(data_)

o/p: [2,4]

map() :
--------
--> map() function will perform on every elements of iterables
syntax -->  map(lambda arguments : expression, iterables)
eg
---

nums = [1,2,3,4,5]
get_ = map(lambda a: a%2 == 0, nums)
print(list(get_))


reduce()
'''

from functools import reduce
nums = [1,2,3,4,5,6]
data_ = reduce(lambda a,b: a%b==0, nums)
print(data_)
