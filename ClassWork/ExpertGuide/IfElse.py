# name = input('enter name ')
# age = int(input('enter age '))
# if age < 18:
#     print('access denied ')
# if age > 18:
#     print('welcome')



#  Second video
# a=int(input("Enter first number "))  
# b=int(input("Enter second number "))  
# c=int(input("enter third number "))  
# if a>b>c:
#     print('a is the greatest', a)  # 4
# elif b>(a>c):
#     print('b is the greatest', b)  # 9
# else:
#     print('c is the greatest', c)  # 6
#                                    # b is the greatest 9

# if a>b and b>c:
#     print('greatest',a)  # Enter first number 6
# elif b>a and b>c:
#     print('greatest',b)  # Enter second number 3
# else:
#     print('greatest',c)  # enter third number 9
#                          # greatest 9
                         
                         


# Third video
while True:
    a=int(input("Enter first no"))
    b= int(input("Enter second no"))
    c= int(input("Enter third no"))
    if a>b and a>c:
        print("a is greatest ",a)
    elif b>a and b > c:
        print('b is greatest', b)
    else:
        print('c is greatest',c)
    reply=input('enter stop to exit')
    if reply =='stop': break
        
        