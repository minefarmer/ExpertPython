# BOOLEAN
a = True
b = False

print('a and b: ', a and b)  # a and b:  False
print('a or b: ',a or b)  # a or b:  True
print('-'*8)  # --------
c = True
d = False

print('a and c or b and d: ', a and c or b and d)  # a and c or b and d:  True
print('a and not b: ', a and not b)  # a and not b:  True

num1 = 4
num2 = 3
print('-'*10)  # ----------
print('Bitwise operations')  # Bitwise operations
print('Bitwise or: ', num1 | num2)  # Bitwise or:  7
print('Bitwise and: ', num1 & num2)  # Bitwise and:  0
print('Bitwise xor: ', num1 ^ num2)  # Bitwise xor:  7

print(num1 == num2)  # False
print(num1 != num2)  # True
