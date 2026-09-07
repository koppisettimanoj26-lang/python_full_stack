<<<<<<< HEAD
'''
Day-3 datatypes and type conversions
1. what are datatypes?
A:  * numeric datatype
        eg: float and integer is called as numeric datatypes
            float : A number which contains decimal values, we call it as a float datatype.
            eg: price = 59.44

            integer : A normal numbers without any decimal values, we call it as a integer.
            eg : num = 3
                 num_2 = 6
    * string :

            Def : -->String is a squence of char that are enclosed in '', "", """"""
                  -->String is immutable.
                  eg : any_ = 'Python is a language'
                       all_ = 'Ab,.&[)-+'
    * list :
            Def : --> List is a collection of different datatypes
                  --> and it is represented by []that are seprated by , ...
                  --> inside the list we call it as items
                  --> list is mutable
                  eg : any_ = [1,'python', [5,6]]
                       print(type(any_))
    * tuple :
             Def : --> Tuple is the collection of different datatypes that are enclosed in () and those are sepated by , ....
                   --> Tuple is immutable.
                   eg : nums = (1,89.67, 'Python', [3,4],(8,9))
    * dictionary :
                    Def : --> Dictionary is a key:value pairs, key and values are seprated by :
                          --> Key and value pair is again call it as an item.
                          --> This item are seprated again with a , ..
                          --> Dictionary is represented using {}
                          --> In key place we can use immutablre datatypes
                          --> In values place we can use any data types
                          eg : {1:2,
                                  'name':'manoj'
                                  (3,4):'tuple'}
                                  print(data_)

    * Set :
            Def : --> Set is a collection of unique elements and set can't allow any duplicate values inside it....
                  --> Set is represented by {} and the elements are seprated by ,
                  eg : an = {1,2,3,3,1}
                       print(an)
                       o/p : {1, 2, 3}
2. What is type conversions?
A: 
    float --> int, str
    eg1 : int()
         price = 45.66
         print(int(price))
         o/p : 45
    Eg2 : price = 46.44
          con = str(price)
          print(type(con))
          o/p : string.
    Eg3 : num = '10.6'
          print(float(a))
    Eg4 : set --> tuple, list
          eg -->
          all_ = {5,6,7}
          print(tuple(all_))
    eg5 : dictionary --> list
          dict()
          details = [('name','teja'),('edu','12th')]
          print(dict(details))
          
'''
details = [('name','teja'),('edu','12th')]
print(dict(details))
=======
'''
Day-3 datatypes and type conversions
1. what are datatypes?
A:  * numeric datatype
        eg: float and integer is called as numeric datatypes
            float : A number which contains decimal values, we call it as a float datatype.
            eg: price = 59.44

            integer : A normal numbers without any decimal values, we call it as a integer.
            eg : num = 3
                 num_2 = 6
    * string :

            Def : -->String is a squence of char that are enclosed in '', "", """"""
                  -->String is immutable.
                  eg : any_ = 'Python is a language'
                       all_ = 'Ab,.&[)-+'
    * list :
            Def : --> List is a collection of different datatypes
                  --> and it is represented by []that are seprated by , ...
                  --> inside the list we call it as items
                  --> list is mutable
                  eg : any_ = [1,'python', [5,6]]
                       print(type(any_))
    * tuple :
             Def : --> Tuple is the collection of different datatypes that are enclosed in () and those are sepated by , ....
                   --> Tuple is immutable.
                   eg : nums = (1,89.67, 'Python', [3,4],(8,9))
    * dictionary :
                    Def : --> Dictionary is a key:value pairs, key and values are seprated by :
                          --> Key and value pair is again call it as an item.
                          --> This item are seprated again with a , ..
                          --> Dictionary is represented using {}
                          --> In key place we can use immutablre datatypes
                          --> In values place we can use any data types
                          eg : {1:2,
                                  'name':'manoj'
                                  (3,4):'tuple'}
                                  print(data_)

    * Set :
            Def : --> Set is a collection of unique elements and set can't allow any duplicate values inside it....
                  --> Set is represented by {} and the elements are seprated by ,
                  eg : an = {1,2,3,3,1}
                       print(an)
                       o/p : {1, 2, 3}
2. What is type conversions?
A: 
    float --> int, str
    eg1 : int()
         price = 45.66
         print(int(price))
         o/p : 45
    Eg2 : price = 46.44
          con = str(price)
          print(type(con))
          o/p : string.
    Eg3 : num = '10.6'
          print(float(a))
    Eg4 : set --> tuple, list
          eg -->
          all_ = {5,6,7}
          print(tuple(all_))
    eg5 : dictionary --> list
          dict()
          details = [('name','teja'),('edu','12th')]
          print(dict(details))
          
'''
details = [('name','teja'),('edu','12th')]
print(dict(details))
>>>>>>> 96d6a7c (PythonClassNotes)
