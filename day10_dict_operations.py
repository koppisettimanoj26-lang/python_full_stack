'''
Dictinory :
--------------
--> Dictionary is collection of key value pair
--> 

Update()
----------
--> Method is used to update a key, incase if the key is not present inside dict then it add that key:value

--> Syntax : dict.update({key : value})

--> there is another way to update a key..
syntax --> dict[key] = value

Eg :


data_ = {'name' : 'Teja',
'balance' : 7000,
'adr' : 1234567,
'pan' : 'fdfoidsfweji',
2 : [3,4]}
print(data_)
data_['Ac'] = 123457
print(data_)

data_.update({'name' : 'sony'})
data_.update({'atmpin' :7899})
print(data_)


Values()
----------
--> values is used to get all the values from the dictionary

Syntax --> dict.values()

eg :

data_ = {'name' : 'Teja',
'balance' : 7000,
'adr' : 1234567,
'pan' : 'fdfoidsfweji',
2 : [3,4]}
print(data_.values())

Keys()
----------
--> Keys is used to get all the keys from the dictionary

syntax --> dict.keys()

eg :

data_ = {'name' : 'Teja',
'balance' : 7000,
'adr' : 1234567,
'pan' : 'fdfoidsfweji',
2 : [3,4]}
print(data_.keys())

items()
---------
--> it is used to display all the key value pair in the dict

syntax --> dict.items()

data_ = {'name' : 'Teja',
'balance' : 7000,
'adr' : 1234567,
'pan' : 'fdfoidsfweji',
2 : [3,4]}
print(data_.items())

clear()
------------
--> It is used to del entire data from the dictionary

--> Syntax : dict.clear()


data_ = {'name' : 'Teja',
'balance' : 7000,
'adr' : 1234567,
'pan' : 'fdfoidsfweji',
2 : [3,4]}
print(data_)
del data_['adr']
print(data_)
print(data_.clear())

if statement
-----------------

--> if condition become true, then it will excute inside block of code...
--> incase it become false, then it will never enter into inside block...

Eg1:
--
age = 15
if age>=18:
    print('eligible to vote')
print(age)

Eg 2:
age = 19
if age>=18:
    print('eligible to vote')
print(age)

Eg 3:
a,b = 19,23
if a>b:
    print('eligible to vote')


if-else:
--------------------
--> else for if statement is a fall-back statement, incase if condition is false then else block will excute... 

eg 1 :
age = 15 
if age>=18:
   print(f'your{age}eligiable to vote')
else:
    print(f'your age is {age} and you have wait for{18-age} years')

eg 2:
a,b = 19,23
if a>b:
    print(a)
else :
    print(b)


-------

'''
age = 15 
if age>=18:
   print(f'your{age}eligiable to vote')
else:
    print(f'your age is {age} and you have wait for{18-age} years')

a,b = 19,23
if a>b:
    print(a)
else :
    print(b)


