# x = 11  # global
# def first():
#     y = 22  #local to first() nonlocal to second()
#     print('y: ',y)  # y:  22
#     def second():
#         z = 33 # local
#         print('z: ',z)  # z:  33
#         print(x)  # 11
#     second()
# first()


# scope of variables

# x = 11 # global to entire file
# def first():
#     # x = 22 local to first. nonlocal to second
#     # here x is a new variable only in the scope of 'first'
#     x = 22
#     print(x)
#     def second():
#         # nonlocal is 3.x specific
#         # here x is a new variable only in the scope of 'second'
#         # global x
#         x = 33
#         print(x)
#     second()
    
# # accessing global x
# print(x)  # 11

# # calling function
# first()

# # calling function value of global x will be:
# print(x)  # 11



x = 11  # global
def f():
    return x
def g():
    x=22
    return x
class h():
    x=33
    def I(self):
        x=44
        print(x)
        self.x=55

print('global(module: ',x)  # global(module:  11
print('x when f is called: ',f())  # x when f is called:  11
print('x when g is called: ',g())  # x when g is called:  22
print('global x remains the same: ',x)  # global x remains the same:  11
obj=h()
print('x in class: ',obj.x)  # x in class:  33
obj=h()
print('attach attribute name x to instance now: ',obj.x)  # attach attribute name x to instance now:  33

print('x in class remain same: ',h.x)  # x in class remain same:  33
    