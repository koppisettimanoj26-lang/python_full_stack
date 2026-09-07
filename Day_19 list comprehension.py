'''
List comprehension
----------------------
--> list comprehension is the short form of syntax to create a list
--> syntax 1--> [expression loop condition]
--> syntax 2--> []

old = [1,2,3,5,8]
new = [i for i in old if i%2 == 0]
print(new)


 nested comprehension
 ---------------------
 --> using list comprehension generting list inside list

any_ = [[i*j*k  for i in range(1,3)] for j in range(1,10)]
print(any_)

of = [[1,2,3],
      [4,5,6],
      [7,8,9]]
data = [num for i in of for num in i]
print(data)
 o/p: [1, 2, 3, 4, 5, 6, 7, 8, 9]

Generator:
--------------

-->Generator is a special function which generates one value at a time
 
'''
def all():
    for j in range(10):
        yield j
j = all()
print(next(j))
print(next(j))
print(next(j))
print(next(j))
