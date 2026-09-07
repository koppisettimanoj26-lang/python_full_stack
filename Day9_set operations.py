'''
Sets --> 



operations
-----------
* union() --> The union() will combine two sets into a single set

--> Syntax : set1.union(set 2) or set1| set2


Eg : 

data_ = {1,2,3,4}
nums  = {4,5,6}
print(data_.union(nums))
print(data_ | nums)

-------------------------------------------------------

* Intersection() --> This will give us the common elements from both sets
--> Syntax : set_1.intersection9(set_2) or set_1 & set_2

eg :

data_ = {1,2,3,4}
nums = {4,5,6}
print(data_.intersection(nums))
print(data_ & nums)

---------------------------------------------------

* Difference() --> It will dispay the different elements from set_1, but not the set_2 elements

-->Syntax : set_1.difference(set_2) or set_1 - set_2

Eg:

data_ = {1,2,3,4}
nums = {4,5,6}
print(data_.difference(nums))
print(data_ - nums)

----------------------------------------------------------------------------------------------------------------------

* Symmetric_difference()
-----------------------------------------------
--> Difference elements from the both
--> Syntax : set_1.symmetric_difference(set_2) or set_1 ^ set_2

Eg :
data_ = {1,2,3,4}
nums = {4,5,6}
print(data_.symmetric_difference(nums))
print(data_ ^ nums)

---------------------------------------------------------------------------------------------------------------------------

Methods :
------------
add() : add() method will add only one element at a time
syntax : set.add(element)

Eg :

data_ = {1,2,3,4}
print(data_)
data_.add(7)
print(data_)

--------------------------------------------------------------------------------------------

update() : We can add more one element s by using update method
Syntax --> set.update([elements]) or set_1.update(set_2)

Eg :
data_ = {1,2,3,4}
nums = {4,5,6}
print(data_)
data_.update([8,9])
print(data_)
data_.update(nums)
print(data_)
print(data_)

--------------------------------------------------------------------------------------------------------

remove() : remove() will delete the given element from the set if the element is not present in the set, it will rise error
syntax --> set.remove(element)

Eg :

data_ = {1,2,3,4}
data_.remove(3)
print(data_)
data_.remove(5)
print(5)

o/p :

{1, 2, 4}

---------------------------------------------------------------------------------------------------

discard() : discard() is used to delete the elements from the set, but never raise any error even the elements not inside set
syntax --> set.discard(element)

eg:

data_ = {1,2,3,4}
data_.discard(7)
print(data_)
data_.discard(1)
print(data_)

o/p :
{1, 2, 3, 4}
{2, 3, 4}

-----------------------------------------------------------------------------------------

clear() :


'''

data_ = {1,2,3,4}
print(data_)
data_.clear()
print(data_)
