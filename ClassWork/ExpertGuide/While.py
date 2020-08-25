# a = 1
# b = 5
# while a<b:
#     print(a)  # 1
#                 # 2
#                 # 3
#                 # 4
#     a=a+1




# Third video
# while True:
#     a=int(input("Enter first no "))
#     b= int(input("Enter second no "))
#     c= int(input("Enter third no "))
#     if a>b and a>c:
#         print("a is greatest ",a)
#     elif b>a and b > c:
#         print('b is greatest ', b)
#     else:
#         print('c is greatest ',c)
#     reply=input('enter stop to exit ')
#     if reply =='stop': break




# while  else
print('check whether a number is prime or not')
number = int(input('enter a number '))
x = int(number/2)
while x >1:
    if number%x == 0:
        print(number, 'has factor', x)
        break
    x = x -1
else:
    print(number ,'is a prime number')