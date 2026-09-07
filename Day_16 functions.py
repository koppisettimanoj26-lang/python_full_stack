'''
Functions
----------
--> A function is block of code that can be executed only when it is called.....
--> A function start with the def keyword and the line called as defination line, where we can define a fun name..
--> And if we want to execute the program in the function, need to call with the function name define at def line


Syntax
----------

def funn_name(parameters):
    pass
funn_name(arguments)

eg:
--
def add_(a,b):
    print(a+b)
all_ = add_(5,6)
print(all_)

Arguments
---------
Positional Arguments
----------------------
--> The arguments should me exact number same at def line and calling, in case if they are not same number will raise an error

Eg:
---
def series_(a,b):
    user = int(input('enter number'))
    print(a,b, end = ' ')
    sums = 0
    for i in range(1,user):
        sums = a+b
        a = b
        b = sums
        print(sums, end = ' ')
        
series_(0,1)

Defalut Arguments
----------------------

--> The defalut arguments where the function will only consider the data at calling, even though data present at the def line
def feb_(num, num2):
    print(num + num2)
feb_(5,4)

def data_(a = 8, b = 9):
    print(a+b)
data_(1,2)

eg
------
def pr_(a=10):
    count = 0
    for i in range(1,a+1):
        if(a%i == 0):
            count += 1
    if count == 2:
        print(f'{a} is prime number')
    else:
        print(f'{a} is not a prime number')
pr_(a = int(input('enter a number')))

Keyword argument
-------------------

--> Keyword arguments are sending aruguments in a pair(a=2), and the passing order is not considered 

def data_(age, name, batch, location):
    print(name)
    print(age)
    print(batch)
    print(location)
data_(name = 'teja', age=45, location='vizag', batch = 6)

Variable length argument
------------------------
--> Adding a (* call it as args) before a variable at parameters we can pass tuple of arguments and can be access with indexing..
eg
---

def all_(*name):
    print(name)
all_('teja','manoj','etc')


keyword length arguments
--------------------------
--> Addinga (** ) before a variable at parameters we can pass key_pair values in the arguments and can be access with .keys(), .values()
'''
def Details(**data_):
    print(data_)

Details(Name = 'Manoj', age = '23', location = 'vizag', batch = 6)






























