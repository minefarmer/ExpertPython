a = 3
b = a
a = 4
print('value of b willnot change ',b)  # value of b will not change  3

L1 = [1,2,3] # a mutable objectLl2 = L1   # make a reference to the same object
L2 = L1
L1[0] = 4 # an inplace change
print('L1: ',L1)  # L1:  [4, 2, 3]
print('L2: ',L2)  # L2:  [4, 2, 3]
# =====================================================================

l1 = [1,2,3]
l2 = l1[:]  # make a copy of l1 or list l1
print('l1: ',l1)  # l1:  [1, 2, 3]
print('l2: ',l2)  # l2:  [1, 2, 3]
