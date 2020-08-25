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

x = 11 # global to entire file
def first():
    # x = 22 local to first. nonlocal to second
    # here x is a new variable only in the scope of 'first'
    x = 22
    print(x)
    def second():
        # nonlocal is 3.x specific
        # here x is a new variable only in the scope of 'second'
        # global x
        x = 33
        print(x)
    second()
    
# accessing global x
print(x)  # 11

# calling function
first()

# calling function value of global x will be:
print(x)  # 11
    
    