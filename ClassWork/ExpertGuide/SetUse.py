'''SETUSE

'''
# 
# 
# 
# 
# 
# 
# # filter duplicates
# l = (1,2,3,4,1,2,3,5)
# l = list(set(1))
# print("List after removing duplicates: ",1)  # List after removing duplicates:  1

# isolate differiences
s = set([1,3,5,7])-set([1,2,4,5,6])
print(s)  # {3, 7}
s = set('abcdefg')-set('abcdefg')
print(s)  # set()

# # order-neutral equality test
# l1 = [1,3,5,2,4]
# l2 = [1,2,3,4,5]
# print(11 == 12)  # False
# print(set(l1) ==set(12))  # Traceback (most recent call last):
#                         # File "/home/carl/Github/ExpertPython/ClassWork/ExpertGuide/SetUse.py", line 25, in <module>
#                         #     print(set(l1) ==set(12))
#                         # TypeError: 'int' object is not iterable

# dealing with large datasets
