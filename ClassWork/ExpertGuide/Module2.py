# first way to import
import Module1

# use fully qualified name
print(Module1.x)  # 22
Module1.message(2)  # Module  2

# second way
from Module1 import *
print(x)  # 22
message(2)  # Module  2

# third way
from Module1 import x,message

print(x)  # 22
message(2)  # Module  2
