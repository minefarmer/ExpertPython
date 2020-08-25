def f(a):
    a = 2
    print(a)
b = 3
f(b)  # 2
print(b)  # 3

def changer(a):
    a[0]=4

l = [1,2,3]
print('l before function call: ',l) # l befor function call:  [1, 2, 3]
changer(l)
print('l after function call: ',l)  # l after function call:  [4, 2, 3]
