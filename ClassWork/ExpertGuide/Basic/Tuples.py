# TUPLES
T=(1,3,4,4,'hi')
print('tuple T: ',T)  # tuple T:  (1, 3, 4, 4, 'hi')

# Indexing
print('T[0]: ',T[0])  # T[0]:  1

# length of tuple
print('length of tuple: ',len(T))  # length of tuple:  5

# if I do not use ',' here, it will treat it as a string
print('concatenation: ', T + ('hi',))  # concatenation:  (1, 3, 4, 4, 'hi', 'hi')

# tuples are inmutible
print('Tuple: ',T)  # Tuple:  (1, 3, 4, 4, 'hi')

# slicing
print(T[1:4])  # (3, 4, 4)
T=(2,3,) + T[1:]
print('now tuple T is:' , T)  # now tuple T is: (2, 3, 3, 4, 4, 'hi')
print('now length of tuple is: ',len(T))  # now length of tuple is:  6

# methods of tuples 
# ttoknow the position of an item
print(('position of 3 in tuple T is: ' ,T.index(3)))  # ('position of 3 in tuple T is: ', 1)

# counting the occurence of an item
print('no of 4 in tuple: ',T.count(4))  # no of 4 in tuple:  2

# nesting
T = (5,6,[7,8,[12.13]],9,('hi', 'python'),{'a':'b'})
print('Tuple: ',T)  # Tuple:  (5, 6, [7, 8, [12.13]], 9, ('hi', 'python'), {'a': 'b'})
T[2][0]=0
print('Tuple: ',T)  # Tuple:  (5, 6, [0, 8, [12.13]], 9, ('hi', 'python'), {'a': 'b'}
print('T[2]: ',T[2])  # T[2]:  [0, 8, [12.13]]
print('T[2][2]: ',T[2][2])  # T[2][2]:  [12.13]
print('T[2][2][1]: ',T[2][2][1])  # Traceback (most recent call last):
  File "/home/carl/Github/ExpertPython/ClassWork/ExpertGuide/Tuples.py", line 37, in <module>
    print('T[2][2][1]: ',T[2][2][1])
IndexError: list index out of range

