# # second video   26

# # first video 
# # lambda returns a function
# # assigning name to function returned is optional

# print((lambda x,y,z: x+y+z)(2,3,4))  # 9

# # here we are assigning name to the function returned

# f = lambda x,y,z: x+y+z

# # calling the function and storing the result
# result = f(2,3,4)
# print(result)  # 9

# # same task using def statement
# def f(x,y,z):
#     return x+y+z

# result = f(2,3,4)
# print(result)  # 9



# jump table

L = [lambda x: x**2,    # Inline function defination
     lambda x: x**3,
     lambda x: x**4]    # A list of three callable functions

for f in L:
    print(f(2))  # 4
                # 8
                # 16
print("*"* 50)  # **************************************************
print(L[2](3))  # 81
print(L[0](4))  # 16

print('_'*50)  # __________________________________________________

def f1(x):      # defined named functions
    return x**2

def f2(x):
    return x**3

def f3(x):
    return x**4

L = [f1,f2,f3]      # Reference by name

for f in L:
    print(f(2))  # 4
                # 8
                # 16

print(L[1](3))  # 27

print("*"* 50)  # **************************************************

key = 'got'
print({'already':(lambda: 2 + 2),  # 8
       'got':(lambda: 2 * 4),
       'one':{lambda: 2 ** 6}}[key]())

# Implimenting by using def

def f1():
    return 2+2

def f2():
    return 2*4

def f3():
    return 2**6

key = 'one'
print({'already':f1,
       'got':f2,
       'one':f3,}[key]())  # 64
key = 'got'
print({'already':(lambda: 2 + 2),
       'got':(lambda: 2 * 4),
       'one':(lambda: 2 ** 6)}[key]())  # 8