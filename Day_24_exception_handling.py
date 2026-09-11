'''
file handling and exception handling :
--------------------------------------

Exception handling:
--------------------

--> This is the way of handling errors
--> We can write any number of exceptions for one code written at try block

try
-----
--> The try block , where we can write code which may contain error
syntax -->
try:
    code lines

except
---------
--> This will handle error that are rised in the try block
syntax:
except errorname:
    print()
eg:
----
try:
    print(6/0)
    print(num)
except ZeroDivisionError:
    print("this is zero division error")
except NameError:
    print('NameError')

else:
-------
--> The else block will only excute, if no error at try block
eg:
---

num = 4
try:
    print(num)
    print(6/1)
except ZeroDivisionError:
    print("this is zero division error")
except NameError:
    print('NameError')
else:
    print('no error')

Finally:
-----------
--> This block will execute regradless with the error at try block

eg:
--

try:
    print(num)
    print(6/1)
except ZeroDivisionError:
    print("this is zero division error")
except NameError:
    print('NameError')
else:
    print('no error')
finally:
    print('hello')

---------------------------------------------------------------------

File handling:
----------------
--> The file handler is a object, which is used to create, update, read, and delete...

modes
-------

r-read
w-write
a-append
x-create

functions
-----------
read()
write()
append()

with open('dem.txt','r') as file:
    print(file.read())
'''

