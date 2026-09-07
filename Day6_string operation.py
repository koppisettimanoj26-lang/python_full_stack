<<<<<<< HEAD
'''
strings
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
operations :
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Indexing : Indexing is used to get char that you looking to access..
   * positive indexing : Positive indexing start from 0 index..
                         syntax--> print(variable_name[index_position])
                         eg:text = 'python'
                                   print(text[3])
                                   o/p : h
                
   * negative indexing : Negetive indexing starts from -1 index..
                         syntax--> print(variable_name[negetive index position])
                         eg2:text = 'python'
                                    print(text[-1])
                                    o/p : n
-------------------------------------------------------------------------------------------------------------
    *len() : len() is a built in function which used to get the no. of char present in the string..
             syntax--> len(variable_name)
             eg:text = 'python is a programming language'
                        print(len(text))
                        o/p : 32

--------------------------------------------------------------------------------------------------------------
    *slicing : This used to access the particular part from the string..
               Syntax --> variable_name[start : end]
               eg : text = 'python is a programming language'
                    print(text[12:23])
                    print(text[:23])
                    print(text[12:])
                    o/p : programming
                          python is a programming
                          programming language

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    *upper() : This is used to convert all the small char into captial
               Syntax --> print(variable_name.upper())
               Eg : text = 'python is a programming language'
                    print(text.upper())
                    o/p : PYTHON IS A PROGRAMMING LANGUAGE

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    *lower() : This used to convert all the capital letter into small.
               Syntax --> print(variable_name.lower())
               eg: text = 'PYTHON IS A PROGRAMMING LANGUAGE'
                   print(text.upper())
                   o/p : python is a programming language

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    *index() : This is used to return the position of char where it is present..
               Syntax : --> print(text.index('substring, start, end))
               Eg : text = 'PYTHON IS A PROGRAMMING LANGUAGE'
                            print(text.index('I'))
                            o/p : 7
                            
               Eg2 : text = 'PYTHON IS A PROGRAMMING LANGUAGE'
                             print(text.index('I',9,25))
                             o/p : 20
                             
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    *replace() : This used to replace the old substring with new substring
                 Syntax --> variable_name.replace(old,new)
                 Eg : text = 'python is a programming language'
                      print(text.replace('python', 'java'))
                      o/p : java is a programming language

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    *split() : This is used to seperate string based on the given substring
               syntax --> variable_name.split(substring)
               Eg : text = 'python is a programming language'
                    print(text.split(' '))
                    o/p : ['python', 'is', 'a', 'programming', 'language']

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    *count() : This is used to count number of occurances of an substring...
               Syntax --> variable_name.count('substring', start, end)
               Eg : text = 'python is a programming language'
                    print(text.count('a'))
                    o/p : 4

              Eg : text = 'python is a programming language'
                   print(text.count('a', 8,16))
                   o/p : 1
'''
'''
text = 'python is a programming language'
count = 0
for i in range(len(text)) :
    if text[i] == ' ' :
        count +=1
print(count)
'''
text = 'python is a programming language'
count = 0

for i in range(len(text)):
    if text[i] == ' ' | 'null':
        count += 1

print(count)
=======
'''
strings
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
operations :
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Indexing : Indexing is used to get char that you looking to access..
   * positive indexing : Positive indexing start from 0 index..
                         syntax--> print(variable_name[index_position])
                         eg:text = 'python'
                                   print(text[3])
                                   o/p : h
                
   * negative indexing : Negetive indexing starts from -1 index..
                         syntax--> print(variable_name[negetive index position])
                         eg2:text = 'python'
                                    print(text[-1:])
                                    o/p : n
-------------------------------------------------------------------------------------------------------------
    *len() : len() is a built in function which used to get the no. of char present in the string..
             syntax--> len(variable_name)
             eg:text = 'python is a programming language'
                        print(len(text))
                        o/p : 32

--------------------------------------------------------------------------------------------------------------
    *slicing : This used to access the particular part from the string..
               Syntax --> variable_name[start : end]
               eg : text = 'python is a programming language'
                    print(text[12:23])
                    print(text[:23])
                    print(text[12:])
                    o/p : programming
                          python is a programming
                          programming language

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    *upper() : This is used to convert all the small char into captial
               Syntax --> print(variable_name.upper())
               Eg : text = 'python is a programming language'
                    print(text.upper())
                    o/p : PYTHON IS A PROGRAMMING LANGUAGE

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    *lower() : This used to convert all the capital letter into small.
               Syntax --> print(variable_name.lower())
               eg: text = 'PYTHON IS A PROGRAMMING LANGUAGE'
                   print(text.upper())
                   o/p : python is a programming language

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    *index() : This is used to return the position of char where it is present..
               Syntax : --> print(text.index('substring, start, end))
               Eg : text = 'PYTHON IS A PROGRAMMING LANGUAGE'
                            print(text.index('I'))
                            o/p : 7
                            
               Eg2 : text = 'PYTHON IS A PROGRAMMING LANGUAGE'
                             print(text.index('I',9,25))
                             o/p : 20
                             
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    *replace() : This used to replace the old substring with new substring
                 Syntax --> variable_name.replace(old,new)
                 Eg : text = 'python is a programming language'
                      print(text.replace('python', 'java'))
                      o/p : java is a programming language

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    *split() : This is used to seperate string based on the given substring
               syntax --> variable_name.split(substring)
               Eg : text = 'python is a programming language'
                    print(text.split(' '))
                    o/p : ['python', 'is', 'a', 'programming', 'language']

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    *count() : This is used to count number of occurances of an substring...
               Syntax --> variable_name.count('substring', start, end)
               Eg : text = 'python is a programming language'
                    print(text.count('a'))
                    o/p : 4

              Eg : text = 'python is a programming language'
                   print(text.count('a', 8,16))
                   o/p : 1
'''
'''
text = 'python is a programming language'
count = 0
for i in range(len(text)) :
    if text[i] == ' ' :
        count +=1
print(count)

text = 'python is a programming language'
count = 0

for i in range(len(text)):
    if text[i] == ' ' | '%':
        count += 1

print(count)

text = 'python'
print(text[:-3])

'''
text = 'python is a la nguage'
count = 0

for i in range(len(text)):
    if text[i] == ' ':
        count += 1

print(count+1)

>>>>>>> 96d6a7c (PythonClassNotes)
