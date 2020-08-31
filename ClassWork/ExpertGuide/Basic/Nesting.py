# def action():
#     # raises unsupported operand type exception
#     print(1+[])
# try:
#     try:
#         action()
#     except TypeError:
#         print('inner try')  # inner try
#     raise TypeError
# except TypeError:
#     print('outer try')  # outer try




def action():
    # raises unsupported operand type exception
    print(1+[])  # 
                # Traceback (most recent call last):
                # File "/home/carl/Github/ExpertPython/ClassWork/ExpertGuide/Nesting.py", line 21, in <module>
                #     action()
                # File "/home/carl/Github/ExpertPython/ClassWork/ExpertGuide/Nesting.py", line 18, in action
                #     print(1+[])
                # TypeError: unsupported operand type(s) for +: 'int' and 'list'
try:
    try:
        action()  # Traceback (most recent call last):
                # File "/home/carl/Github/ExpertPython/ClassWork/ExpertGuide/Nesting.py", line 21, in <module>
                #     action()
                # File "/home/carl/Github/ExpertPython/ClassWork/ExpertGuide/Nesting.py", line 18, in action
                #     print(1+[])
                # TypeError: unsupported operand type(s) for +: 'int' and 'list'
    finally:
        print('inner try')  # inner try
finally:
    print('outer try')  # outer try
    