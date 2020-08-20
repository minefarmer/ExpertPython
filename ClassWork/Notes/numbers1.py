num1=5
num2=7
num3=3
num4=9

# addition = num1 + num2   # 12
# print('sum: ',addition);

# subtraction = num2 - num3  # 4
# print('sum: ',subtraction)

# division = num4 / num1   # 1.8
# print('sum: ',division);

# product = num1 * num2   # 35
# print('sum: ',product);

# precedence
# result = num1 * num2 + num3 * num4   # 62
# print('sum: ',result);

# parenthesis
# result = num1 * (num2 + num3) * num4
# print('Now the result is: ', result)  # Now the result is:  450

#  mixed types are converted up
num5 = 10
num6 = 4
print('num5 + num6: ',num5 + num6)  # num5 + num6:  14
print('num5/num6: ',num5/num6)  # num5/num6:  2.5

# comparision operators are chained
print('comparison: ',num1<num2<num4)  # comparison:  True
print('And operator: ',num1>num2 and num2<num4)  # And operator:  False

# complex number
a = 1 + 2j
b = 2 +3j
print(a+b)  # (3+5j)

# power
cube = 4**3
print('cube of 4 is: ',cube)  # cube of 4 is:  64