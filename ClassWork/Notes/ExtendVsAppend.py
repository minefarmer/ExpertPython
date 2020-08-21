# extend vs append
L=[1,2,3]
L.append([1,2,3])
print(L)  # [1, 2, 3, [1, 2, 3]]
L.extend([1,2,3])
print(L)  # [1, 2, 3, [1, 2, 3], 1, 2, 3]

