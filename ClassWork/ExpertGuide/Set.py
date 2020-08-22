"""SET
"""
set1 = set('abcde')
set2 = set('defgh')

# print set
print('set 1: ',set1)  # set 1:  {'b', 'e', 'c', 'a', 'd'}
print('set 2: ',set2)  # set 2:  {'d', 'f', 'h', 'g', 'e'}

# difference
print('Differience: ',set1 - set2)  # Differience:  {'c', 'b', 'a'}

# Union
print('Union ', set1 | set2)  # Union  {'h', 'c', 'e', 'b', 'a', 'g', 'd', 'f'}

# intersection
print('Intersection: ',set1 & set2)  # Intersection:  {'d', 'e'}

# symmetric difference
print('Symmetric difference ', set1 ^ set2)  # Symmetric difference  {'a', 'c', 'f', 'g', 'b', 'h'}

# superset
print('is set1 a superset of set2: ',set1>set2)  # is set1 a superset of set2:  False

# subset
print('is set1 a subset of set2: ',set1<set2)  # is set1 a subset of set2:  False

# to check whether an object is present in subset
print('is a in set1', 'a' in set1)  # is a in set1 True

