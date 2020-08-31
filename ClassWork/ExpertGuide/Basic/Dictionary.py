# DIFFERIENT WAYS TO CREATE A DICTIONARY
# first   11
# second   16
# third   23
# 
# USING THE DICTIONARY   30
# 
# 
# 
# 
# first
# dictionaried are not ordered
D={'name':'abc' , 'l_name':'xyz' , 'age':22}
print(D)  # {'name': 'abc', 'l_name': 'xyz', 'age': 22}

# second
d={}
d['name']='abc'
d['l_name']='xyz'
d['age']=81
print(d)  # {'name': 'abc', 'l_name': 'xyz', 'age': 81}

# # third
H=dict(name='abc', l_name='ghe', age=44)
print(H)  # {'name': 'abc', 'l_name': 'ghe', 'age': 44}

print(('-'*25))  # -------------------------


# Using the dictionary
# length of dictionary
print('length of dictionary: ',len(H))  # length of dictionary:  3

# print specific value
print((d['name']))  # abc

# adding 1 to age
d['age'] = d['age'] + 1
print(d)  # {'name': 'abc', 'l_name': 'xyz', 'age': 82}

# mutable
d['name']='def'
print(d)  # {'name': 'def', 'l_name': 'xyz', 'age': 82}

# deletion
del d['name']
print(d)  # {'l_name': 'xyz', 'age': 82}

print(d.pop('l_name'))  # xyz
print(d)  # {'age': 82}

print(('-'*25))  # -------------------------
# nesting
record={'name':{'first':'Bob','lname':'Smith'},
        'jobs':['manager','engineer'],
        'age':34}
print(record)  # {'name': {'first': 'Bob', 'lname': 'Smith'}, 'jobs': ['manager', 'engineer'], 'age': 34}
print(record['name']['first'])  # Bob
print(record['jobs'][0])  # manager

print(('-'*25))  # -------------------------
# ovrwrite the previous value if key is the same
x={' ':'1'," " :'2', 'cut':'apple','cut':'bananna'}
print(x)  # {' ': '2', 'cut': 'bananna'}

print(('-'*25))  # -------------------------
# methods of dictionary
print(D.keys())  # dict_keys(['name', 'l_name', 'age'])
print(D.values())  # dict_values(['abc', 'xyz', 22])
print(D.items())  # dict_items([('name', 'abc'), ('l_name', 'xyz'), ('age', 22)])
print(D.get('name')) # abc

