#  This file is not working
 # A simple function
def a_func():
    print("Simple function called")

# Function returning a value
def func_return():
    x = 1
    print('Function returning a value')
    return x

# Function with arguments
def func_arguments(arg):
    print('Function with argument called')
    print(arg)
    
# calling functions
a_func_()

# Storing result of function
y = func_return()
print(y)

# Calling function with differient arguments
func_arguments(4)
func_arguments('Hello')
t = (1,2,3)
func_arguments(t)
