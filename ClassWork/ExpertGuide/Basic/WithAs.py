# with/as statement is designed to be alternative of try/finally statement
# but for particular objects

# on entry check whether file is present or not

# with open(r'sample1.txt') as myfile:  # with open(r'sample1.txt') as myfile:
#                                     # FileNotFoundError: [Errno 2] No such file or directory: 'sample1.txt'
#                                     #     for i in myfile:
#         print(i)
        
# at exit close the file.

# if a file is not present raise error
myfile = open(r'ClassWork/ExpertGuide/Abc.txt')
for line in myfile:
    print(line)  # Hello

                # how are you?