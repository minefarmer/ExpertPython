#List Operations

L =[123, 'welcome' , 456, 'hello']
# indexing
print(L[0])  # 123

# slicing
print(L[:-1])  # [123, 'welcome', 456]

# concatenation
L=L + [ 1,2,3]
print(L)  # [123, 'welcome', 456, 'hello', 1, 2, 3]

print(L*2)  # [123, 'welcome', 456, 'hello', 1, 2, 3, 123, 'welcome', 456, 'hello', 1, 2, 3]

# delete from list
# remove: removes the first matching value, not the specific index
# del: removes a specific index
# pop: returns the removed element
L.remove('hello')
print(L) # [123, 'welcome', 456, 1, 2, 3]

del  L[0]

print(L)  # ['welcome', 456, 1, 2, 3]
print(L.pop(1))  # 456

# s = 'python' 
# s[0]='z
# """
# s ='Python'
# s.append('World')
# strings are not mutable
# """
L.extend(['hi','world'])
print(L)  # ['welcome', 1, 2, 3, 'hi', 'world']

# reverse the list
L.reverse()
print("Reverse list: ",L)  # Reverse list:  ['world', 'hi', 3, 2, 1, 'welcome']

# bound checking
# print L[100]

# nesting
l = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print('nested list')
print(l)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l1 = [1,6,9,6,7]
l1.sort()
print(l1)  # [1, 6, 6, 7, 9]

