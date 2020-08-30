# try:
#     f=open('ClassWork/ExpertGuide/Abc.txt')  # copied relative path
#     a = [1,2,3]
#     print(a[5])  # raises raises exception
#                 # IndexError: list index out of range

# finally:
#     print('Closing file')  # Closing file
#     f.close()
    
# print("Hello")
# # /home/carl/Github/ExpertPython/ClassWork/ExpertGuide/Abc.txt  # copied path 



# try:
#     raise IndexError
# except IndexError:
#     print("got exception")  # got exception
#     raise  # Traceback (most recent call last):
#             # File "/home/carl/Github/ExpertPython/ClassWork/ExpertGuide/Try.py", line 17, in <module>
#             #     raise IndexError
#             # IndexError




class DefinedException(Exception):print("value lesser than 10 is not allowed")  # value lesser than 10 is not allowed

# function outside Exception class
def amethod():
    raise DefinedException
try:
    amethod()
    # raise DefinedException
except DefinedException:
    print('got exception')  # got exception

print('hi there can u see me')  # hi there can u see me
# try:                          #  uncommented this block throughs an error
#     raise(NameError)
# except NameError:
print("induced error")  # induced error
    
    
    
    
# search
l = [1,2,3,4,5,6,7,8,9]
class Failure(Exception):pass

def find():
    x=int(input('enter a no '))  # 11
    if x in l:
        return "position of number",l.index(x)
    else:
        raise Failure()
try:
    s=find()
    print(s)
except Failure:
    print('number not found')  # number not found
    
