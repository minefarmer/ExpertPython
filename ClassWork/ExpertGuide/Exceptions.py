def fetcher(obj,index):
    return obj[index]

try:
    x='Python'
    fetcher(x,7)
    # z = 10/0
    # not executed
    print("Within try") # File "/home/carl/Github/ExpertPython/ClassWork/ExpertGuide/Exceptions.py", line 11
                        
                    #         ^
                    # SyntaxError: unexpected EOF while parsing
                    # ################################################  this only apears without code on lines 15 and 16

except IndexError:
    print("Got exception")  # Got exception
    
print('after try')  # after try

# y = "xyz"
# fetcher(y,7)




class MyBad(Exception):pass
try:
    raise MyBad("sorry my mistake")
except MyBad as x:
    print(x)  # sorry my mistake




# # custom print display
# class Myexception(Exception):
#     def __str__(self):
#         return("my defined print statement")  # my defined print statement
    

# try:
#     raise Myexception()
# except Myexception:
#     print('caught my exception')  # caught my exception
#     print(Myexception())




# custom print display and init
class Myexception(Exception):
    def __init__ (self,y):
        self.y = y
    def __str__(self):
        print(self.y)  # 4  # both line 55 and line 62 must be uncommented for (4) to print
        return("my defined print statement")  # my defined print statement
    
try:
    raise Myexception(4)
except Myexception as x:
    print('caught my exception')  # caught my exception
    print(x)  # 4  # both line 55 and line 62 must be uncommented for (4) to print