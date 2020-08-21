# string operations
s=('jones smith')


# indexing
print(s[0])  # j
print(s[-1])  # h

print(len(s))  # 11

# substring
print(s[1:5])  # ones  ** from s  ^^ line two

# x[i:j:k] means extract all the items in x, from offset i through j-i, by k
print(s[1:10:3])  # osm

# reverse a string
print(s[::-1])  # htims senoj

# concatinate
print(s+' xyz')  # jones smith xyz

# find the index
print(s.find('mi'))  # 7

# uppercase
print(s.upper()) # JONES SMITH

# formating
print('%s like %s' %('i', 'music'))  # i like music

# repalce
print(s.replace('s','x'))  # jonex xmith
print(s.replace('s','x',1)) # jonex smith

