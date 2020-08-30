import math

# # exception not caught in try: 'kill the program'
# def square_root(number):
#     assert number>0 , 'no square for negative numbers'
#     print(math.sqrt(number))

# while True:
#     x=int(input("enter a number "))  # 5  # using a positive number
#                                     # 2.23606797749979
#     square_root(x)


# exception not caught in try: 'kill the program'
def square_root(number):
    assert number>0 , 'no square for negative numbers'
    print(math.sqrt(number))

while True:
    x=int(input("enter a number "))  # -8  # using a negative number
                                    # Traceback (most recent call last):
                                    # File "/home/carl/Github/ExpertPython/ClassWork/ExpertGuide/Assert.py", line 22, in <module>
                                    #     square_root(x)
                                    # File "/home/carl/Github/ExpertPython/ClassWork/ExpertGuide/Assert.py", line 16, in square_root
                                    #     assert number>0 , 'no square for negative numbers'
                                    # AssertionError: no square for negative numbers
                                    #     square_root(x)
