def gensquares1(n):
    for i in range (n):
        yield i ** 2
        
# problem using return statement
def gensquares2(n):
    for i in range(n):
        return i ** 2  # return 0**2
    
# returning a list of result.
def gensquares3(n):
    l =[]
    for i in range(n):
        l.append(i**2)
    return l
print('gensquares1')  # gensquares1

a=gensquares1(5)
print(next(a))  # 0
print(next(a))  # 1
print(next(a))  # 4
print(next(a))  # 9
print(next(a))  # 16

print('gensquares2')  # gensquares2
b=gensquares2 (3)
print(b)  # 0
b = gensquares2 (3)
print(b)  # 0
print('gensquares3')  # gensquares3
c=gensquares3 (3)
print(c)  # [0, 1, 4]