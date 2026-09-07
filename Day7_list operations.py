<<<<<<< HEAD
'''
List
----
--> collection of different datatypes that are seprated by  , and it is represented by[]
* Indexing
-------------
positive --> 0
Negative --> -1

eg : so = [1,2,3,4,'python']
     print(so[-1][-3])
     o/p : h

eg : all_ = [12,[1,'python',[1,4],(78,[6,7]),['java',78]]]
     print(all_[1][3][1][1])
     print(all_[1][3][1])
     o/p : 7,[6,7]

eg3 : all_ = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]
      print(all_[1][2][1][2])
      o/p : t

* Len()
-------------------------
--> THis function is used to find the number of items present inside the list
--> Syntax len(variable_name)

Eg1 : data_ = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]
     print(len(data_))
     o/p : 2

Eg 2: data_ = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]
      print(len(data_[1]))
      o/p : 4

* Slicing
--------------------
Eg : data_ = [1,2,3,4,5,6,7]
     print(data_[2:6])
     o/p : 2,3,4,5,6

* Concatination
---------------------
Eg : a = [2,1]
     b = [3,4]
     print(a+b)


* Methods
--------------------
    * append() : Append method will add new items into the list at last index position
                 Syntax --> Variable_name.append(item)
    Eg : 
        go = [1,2]
        go.append(3)
        print(go)
        go.append(4)
        print(go)
        go.append('python')
        print(go)

        
    * extend() : extend() will add the items into a list at last index position, but it will give each value as one index inside list
                 Syntax --> variable_name.extend(items)

    Eg : go = [2,5]
         go.extend([6])
         print(go)
         o/p : [2,5,6]

* pop() : pop() is used to remove item from the list and it will delete based on the index position
          Syntax : variable_name.pop(inde_position)


    Eg : a =[5,6,4,32,'python']
         a.pop(3)
         print(a)
         o/p : [5,6,4,'python']
    Eg : a =[5,6,4,32,'python']
         a.pop()
         print(a)

* remove() : 


a =[5,6,4,32,'python']
a.remove(4)
print(a)
'''
a =[5,6,4,32,'python']
a.remove(4)
print(a)
=======
'''
List
----
--> collection of different datatypes that are seprated by  , and it is represented by[]
* Indexing
-------------
positive --> 0
Negative --> -1

eg : so = [1,2,3,4,'python']
     print(so[-1][-3])
     o/p : h

eg : all_ = [12,[1,'python',[1,4],(78,[6,7]),['java',78]]]
     print(all_[1][3][1][1])
     print(all_[1][3][1])
     o/p : 7,[6,7]

eg3 : all_ = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]
      print(all_[1][2][1][2])
      o/p : t

* Len()
-------------------------
--> THis function is used to find the number of items present inside the list
--> Syntax len(variable_name)

Eg1 : data_ = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]
     print(len(data_))
     o/p : 2

Eg 2: data_ = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]
      print(len(data_[1]))
      o/p : 4

* Slicing
--------------------
Eg : data_ = [1,2,3,4,5,6,7]
     print(data_[2:6])
     o/p : 2,3,4,5,6

* Concatination
---------------------
Eg : a = [2,1]
     b = [3,4]
     print(a+b)


* Methods
--------------------
    * append() : Append method will add new items into the list at last index position
                 Syntax --> Variable_name.append(item)
    Eg : 
        go = [1,2]
        go.append(3)
        print(go)
        go.append(4)
        print(go)
        go.append('python')
        print(go)

        
    * extend() : extend() will add the items into a list at last index position, but it will give each value as one index inside list
                 Syntax --> variable_name.extend(items)

    Eg : go = [2,5]
         go.extend([6])
         print(go)
         o/p : [2,5,6]

* pop() : pop() is used to remove item from the list and it will delete based on the index position
          Syntax : variable_name.pop(inde_position)


    Eg : a =[5,6,4,32,'python']
         a.pop(3)
         print(a)
         o/p : [5,6,4,'python']
    Eg : a =[5,6,4,32,'python']
         a.pop()
         print(a)

* remove() : 


a =[5,6,4,32,'python']
a.remove(4)
print(a)
'''
a =[5,6,4,32,'python']
a.remove(4)
print(a)
>>>>>>> 96d6a7c (PythonClassNotes)
