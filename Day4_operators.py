<<<<<<< HEAD
'''
Day -4 of python
Concatination
-------------------
A : the + will behave two ways for numerics it works normally and for other datatypes like string, list, tuple it concatinate... 
1. Operators -->
A: The operators are used to perform operations on variables and the values..
    --> 1. Arthematic operator
---------------------------------------------------------------
            eg : +,-,*,/, // ..
            eg1: num = 90
                 num_1 = 7
                 print(num+num_1)
-----------------------------------------------------------------              
            eg2: an = [1,2]
                 of = [3,4]
                 print(an+of)
------------------------------------------------------------------
            eg3 : a =3
                  b =2
                  print(a-b)
--------------------------------------------------------------------
            eg4 : a =3
                  b =2
                  print(a*b)
--------------------------------------------------------------------------
            eg5 : a =8.5
                  b =4.4
                  print(a/b)
            o/p : 1.9318181818181817
------------------------------------------------------------------------------
            eg6 : a =8.5
                  b =4.4
                  print(a//b)(float division means it does not consider the after decimal values )
            0/p : 1.0
   ---------------------------------------------------------------------
    --> 2. Assignment operator
    -------------------------------
            eg : =, +=, -=, *=, %=, /=
            += --> is increment operator
            eg1 : a = 0
                  print(a)
                  a += 1
                  print(a)
            o/p : 0
                  1
------------------------------------------------------------------------------
            eg2 : a = 5
                  print(a)
                  a -= 1
                  print(a)
            o/p : 5
                  4
--------------------------------------------------------------------------------
            eg3 : a = 5
                  print(a)
                  a *= 2
                  print(a)
            o/p : 5
                  10
-------------------------------------------------------------------
            eg4 : a = 4
                  print(a)
                  a %= 2
                  print(a)
            o/p : 5
                  0
-------------------------------------------------------------------
            eg5 : a = 8.5
                  print(a)
                  a /= 4.4
                  print(a)
            o/p : 8.5
                  1.9318181818181817
-------------------------------------------------------------------
    --> 3. comparison operator
    --------------------------------------
        ==, >=, <=, <, >, !=
------------------------------------------------------
        Eg1 : num = 5
              num_1 = 7
              print(num == num_1)
        o/p : False
--------------------------------------------------------
        Eg2 : num = 5
              num_1 = 7
              print(num != num_1)
        o/p : true
----------------------------------------------------
        Eg3 : num = 5
              num_1 = 7
              print(num > num_1)
        o/p : false
------------------------------------------------
        Eg4 : num = 5
              num_1 = 7
              print(num < num_1)
        o/p : true
------------------------------------------------
        Eg5 : num = 5
              num_1 = 7
              print(num <= num_1)
        o/p : true
-------------------------------------------------
        Eg6 : num = 5
              num_1 = 7
              print(num >= num_1)
        o/p : false
------------------------------------------------
    --> 4. logical operator
--------------------------------------------------
        and --> every condition in statement must be true the we will get output as true
---------------------------------------------------------
        Eg1 : num = 9
              num_1 = 13
              print(num >= num_1 and num < 10)#beacause here one condition is correct and the other is false
              print(num<= num_1 and num < 10) #because here two conditions are correct
        o/p : False
              True
----------------------------------------------------------
         Eg2 : num = 9
              num_1 = 13
              print(num >= num_1 or num < 10)#beacause here if we have one condition is true it will return true
         o/p : true    
--------------------------------------------------
    --> 5. Identity operator
--------------------------------------------------
            eg : is, isnot
            eg1: a = [1,2]
                 b = [1,2]
                 print(a is b)
            o/p: false
------------------------------------------------------------
    --> 6. Membership operator
-------------------------------------------------------------
        eg : in, notin
        eg1 : nums = 'python is language'
              print('y' in nums)
              print('i' not in nums)
        o/p : True
              False
-------------------------------------------------------------
    --> 7. Bitwise operator
'''

nums = 'python is language'
print('y' in nums)
print('i' not in nums)
=======
'''
Day -4 of python
Concatination
-------------------
A : the + will behave two ways for numerics it works normally and for other datatypes like string, list, tuple it concatinate... 
1. Operators -->
A: The operators are used to perform operations on variables and the values..
    --> 1. Arthematic operator
---------------------------------------------------------------
            eg : +,-,*,/, // ..
            eg1: num = 90
                 num_1 = 7
                 print(num+num_1)
-----------------------------------------------------------------              
            eg2: an = [1,2]
                 of = [3,4]
                 print(an+of)
------------------------------------------------------------------
            eg3 : a =3
                  b =2
                  print(a-b)
--------------------------------------------------------------------
            eg4 : a =3
                  b =2
                  print(a*b)
--------------------------------------------------------------------------
            eg5 : a =8.5
                  b =4.4
                  print(a/b)
            o/p : 1.9318181818181817
------------------------------------------------------------------------------
            eg6 : a =8.5
                  b =4.4
                  print(a//b)(float division means it does not consider the after decimal values )
            0/p : 1.0
   ---------------------------------------------------------------------
    --> 2. Assignment operator
    -------------------------------
            eg : =, +=, -=, *=, %=, /=
            += --> is increment operator
            eg1 : a = 0
                  print(a)
                  a += 1
                  print(a)
            o/p : 0
                  1
------------------------------------------------------------------------------
            eg2 : a = 5
                  print(a)
                  a -= 1
                  print(a)
            o/p : 5
                  4
--------------------------------------------------------------------------------
            eg3 : a = 5
                  print(a)
                  a *= 2
                  print(a)
            o/p : 5
                  10
-------------------------------------------------------------------
            eg4 : a = 4
                  print(a)
                  a %= 2
                  print(a)
            o/p : 5
                  0
-------------------------------------------------------------------
            eg5 : a = 8.5
                  print(a)
                  a /= 4.4
                  print(a)
            o/p : 8.5
                  1.9318181818181817
-------------------------------------------------------------------
    --> 3. comparison operator
    --------------------------------------
        ==, >=, <=, <, >, !=
------------------------------------------------------
        Eg1 : num = 5
              num_1 = 7
              print(num == num_1)
        o/p : False
--------------------------------------------------------
        Eg2 : num = 5
              num_1 = 7
              print(num != num_1)
        o/p : true
----------------------------------------------------
        Eg3 : num = 5
              num_1 = 7
              print(num > num_1)
        o/p : false
------------------------------------------------
        Eg4 : num = 5
              num_1 = 7
              print(num < num_1)
        o/p : true
------------------------------------------------
        Eg5 : num = 5
              num_1 = 7
              print(num <= num_1)
        o/p : true
-------------------------------------------------
        Eg6 : num = 5
              num_1 = 7
              print(num >= num_1)
        o/p : false
------------------------------------------------
    --> 4. logical operator
--------------------------------------------------
        and --> every condition in statement must be true the we will get output as true
---------------------------------------------------------
        Eg1 : num = 9
              num_1 = 13
              print(num >= num_1 and num < 10)#beacause here one condition is correct and the other is false
              print(num<= num_1 and num < 10) #because here two conditions are correct
        o/p : False
              True
----------------------------------------------------------
         Eg2 : num = 9
              num_1 = 13
              print(num >= num_1 or num < 10)#beacause here if we have one condition is true it will return true
         o/p : true    
--------------------------------------------------
    --> 5. Identity operator
--------------------------------------------------
            eg : is, isnot
            eg1: a = [1,2]
                 b = [1,2]
                 print(a is b)
            o/p: false
------------------------------------------------------------
    --> 6. Membership operator
-------------------------------------------------------------
        eg : in, notin
        eg1 : nums = 'python is language'
              print('y' in nums)
              print('i' not in nums)
        o/p : True
              False
-------------------------------------------------------------
    --> 7. Bitwise operator
'''

nums = 'python is language'
print('y' in nums)
print('i' not in nums)
>>>>>>> 96d6a7c (PythonClassNotes)
