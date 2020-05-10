#Arrays

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
2
fruits.count('tangerine')
0
fruits.index('banana')
3
fruits.index('banana', 4)  # Find next banana starting a position 4
6
fruits.reverse()
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
'pear'


stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
[3, 4, 5, 6, 7]
stack.pop()
7
stack
[3, 4, 5, 6]
stack.pop()
6
stack.pop()
5
stack
[3, 4]


 from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue
deque(['Eric', 'John', 'Michael'])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
'Eric'
queue.popleft()
'John'
queue
deque(['Michael', 'Terry', 'Graham'])


# to use comprehensions 

numbers=[24,3,31,6]
[element + 1 for element in numbers]
[25, 4, 32, 7]
"""def lambdaexpr = lambda(x:x+1)
  File "<stdin>", line 1
    def lambdaexpr = lambda(x:x+1)
                   ^
SyntaxError: invalid syntax
lambdaexpr = lambda(x:x+1)
  File "<stdin>", line 1
    lambdaexpr = lambda(x:x+1)
                       ^
SyntaxError: invalid syntax"""
# Full form of comprehension 

lambdaexpr = lambda x:x+1
sumlist =list(map(lambdaexpr,numbers))
sumlist
[25, 4, 32, 7]
[abs(element) for element in numbers]
[24, 3, 31, 6]
[ x >20 for x in numbers]  #Condition check 
[True, False, True, False]
[x for x in numbers if x > 20]  # Filter 
[24, 31]
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# to access all elements 

[ x for row in matrix for x in row]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
transpose=[]
"""
for colms in range(4):
    transpose_row=[]
    for row in matrix
  File "<stdin>", line 3
    for row in matrix
                    ^
SyntaxError: invalid syntax"""
# To implement transpose function 

for colms in range(4):
    transpose_row=[]
    for row in matrix:
        transpose_row.append(row[colms])
    transpose.append(transpose_row)

transpose
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
"""
transpose.clear
<built-in method clear of list object at 0x000001711C488D48>"""

transpose
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
transpose.clear()
transpose
[]
for colitr in range(4):
    transpose.append([row[colitr] for row in matrix])

transpose
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

#Transponse by using Nested comprehension 
"""
[[row[colitr] for row in matrix] colitr for colitr in range(4)]
  File "<stdin>", line 1
    [[row[colitr] for row in matrix] colitr for colitr in range(4)]
                                          ^
SyntaxError: invalid syntax
[colitr for colitr in range(4)]
[0, 1, 2, 3]
[colitr for colitr in range(4) [row[colitr] for row in matrix] ]
  File "<stdin>", line 1
    [colitr for colitr in range(4) [row[colitr] for row in matrix] ]
                                                  ^
SyntaxError: invalid syntax"""

[[row[colitr] for row in matrix]  for colitr in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# Zip(*itr) will go through all rows and concatinate them 
list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
list(zip(matrix))
[([1, 2, 3, 4],), ([5, 6, 7, 8],), ([9, 10, 11, 12],)]
list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]


#Tuple Sequence 
tupleex = (1,2,3)
tupleex
(1, 2, 3)
"""tconcat = tupleex,(string1,string3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'string1' is not defined"""

tconcat = tupleex,("string1","string3")

tconcat
((1, 2, 3), ('string1', 'string3'))
#Can access the elements individually 
tupleex[1]
2

# Can't modify the element in the tuple as they are immutable 
"""
tupleex[1]=24
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment"""

# List in tuple
listintuple = ([1,2,3,4],[5,6,7,8])
listintuple[0]
[1, 2, 3, 4]
listintuple[0][1]
2
len(tupleex)
3
len(tconcat)
2
x=24
y=3
sum='sahasra'

t=24,3,'sahasra'
len(t)
3

# Return the elements from tuple 
x1,y1,sum1 = t

#Verification 
sum1 == sum
True

# Sets 
setex ={1,2,3,1}
setex
{1, 2, 3}

setwithdiffdatatype={24,'dinesh'}

# Set operations
b = set('alacazam')
a = set('abracadabra')
a
{'c', 'b', 'r', 'd', 'a'}
b
{'c', 'z', 'l', 'm', 'a'}

# Intersect which is common in both
a & b
{'c', 'a'}

# Distinct elements of both a and b
a | b
{'c', 'b', 'z', 'r', 'd', 'l', 'm', 'a'}

# Elements of only in b and not exits in a
b - a
{'z', 'l', 'm'}

# Elements exits in a or b both not common
b^ a
{'r', 'd', 'b', 'z', 'l', 'm'}
a^b
{'r', 'd', 'b', 'z', 'l', 'm'}

# Can use comprehensions to form a set 
listexp = [x for x in 'abracadabra' if x not in 'abc']
setexp ={x for x in 'abracadabra' if x not in 'abc'}
listexp
['r', 'd', 'r']
setexp
{'r', 'd'}




# Dictionaries 

nameinfo = {'dinesh': 8505, 'sasi': 8903}
# can add a new element 
nameinfo['sahasra']= 1804
#can look up for an element 
'sasi' in nameinfo
True


# Dictionary created using comprehension 

{x:x**2 for x in (2,4,6)}
{2: 4, 4: 16, 6: 36}


#Looping techniques

for key,value in nameinfo.items():
    print(key,value)

dinesh 8505
sasi 8903

# Ienumerate 

for index,value in enumerate(['tic', 'tac', 'toe']):
    print(index,value)

0 tic
1 tac
2 toe

# Can use zip to iterate both collections at once 

questions = ['name', 'quest', 'favorite color']
answers = ['dinesh', 'eco friendly', 'white']

for itr1,itr2 in zip(questions,answers):
    print('What is your {0}?  It is {1}.'.format(itr1, itr2))

What is your name?  It is dinesh.
What is your quest?  It is eco friendly.
What is your favorite color?  It is white.


# Zip only combines untill the same count ,so added an extra in answers which printed above

answers.append('black')
for itr1,itr2 in zip(questions,answers):
    print('What is your {0}?  It is {1}.'.format(itr1, itr2))

What is your name?  It is dinesh.
What is your quest?  It is eco friendly.
What is your favorite color?  It is white.


# Removed one and added element in questions 
answers
['dinesh', 'eco friendly', 'white', 'black']
questions.append('sport')
answers.pop()
'black'
for itr1,itr2 in zip(questions,answers):
    print('What is your {0}?  It is {1}.'.format(itr1, itr2))

What is your name?  It is dinesh.
What is your quest?  It is eco friendly.
What is your favorite color?  It is white.
questions
['name', 'quest', 'favorite color', 'sport']

# Sort form of collection with out duplicates

basket=['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for item in sorted(set(basket)):
    print (item)

apple
banana
orange
pear


# Sequence comparsions, it is done based on lexicographical ordering ..one set of comparsion and followed by next
# Unicode comparsions

arr1 =[1,2,3]
arr2 =[1,2,4]
arr1 < arr2
True

# string comparsions
'A' < 'a'
True

strarr1=['a','b','c']
strarr2=['a','b','A']
strarr1 > strarr2
True

# Comparsions should be of same type or else will get type error
intarr1=[1,2,3]
mixarr1=['a',1,'b']
intarr1 < mixarr1
"""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'int' and 'str'"""


