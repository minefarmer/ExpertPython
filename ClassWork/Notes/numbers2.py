import math
import random
import fractions

# closest number below value
print(math.floor(12.6))  # 12
print(math.floor(-12.6))  # -13

# truncate fractional part
print(math.trunc(12.6))  # 12
print(math.trunc(-12.6))  # -12

# square root of a number
print(math.sqrt(256))  # 16

# random floats between 0 and 1
a = (random.random())
print(round(a,2))  # 16.0  ** second run  # 0.26

# selecting a random integer between two numbers
print(random.randint(2, 8))  # 3

frac1 = fractions.Fraction(5,6)
print('First fraction: ',frac1)  # 5/6
frac2 = fractions.Fraction(2,6)
print('Second fraction: ',frac2)  # 1/3
print("Sum: ",frac1 + frac2)  # 7/6
