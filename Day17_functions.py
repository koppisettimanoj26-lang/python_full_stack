'''
Scope of variables
---------------------
1. Local variable : A variable is define inside the function call it as call variable, where the variable can only access with in that function
   ---------------
Eg:
----
def display():
    name = 'teja'
    print(name)
display() print(name)

    o/p : error because the name variable is decleared in the function but
    whenever the function completes the name variable will delete from the
    memory so when we print the name outside the function there will be no
    variable called name so will get error

    
2. Global variable : A variable that is defined outside the function and it can be access anywhere through out the programm...
   ---------------
Eg:
----
a=90
print(a)
def display():
    a = 10 
display()
print(a)

o/p : 90,90

3. Global keyword : Global is a keyword used to reaccess new values to variable that was already define outside the function call
   --------------
Eg:
---
a=90
print(a)
def display():
    global a
    a = 10 
display()
print(a)

o/p : 90,10

4. Passing by value :
-----------------------
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

even_odd(10)

5. pass by variable :
------------------------
num = 7
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

even_odd(num)

6. Recursive function :
-------------------------


'''

def c(a):
    if a == 0 or a == 2:
        return a
    return a * c(a-1)
print(c(5))

