# files
# open a file in write mode
f=open('practice.txt','w')

# writing content to files
f.write("Hello\nhow are you\nAre you comming tommorow\n")
f.write('ya i will be there!')

# close file
f.close()

# open file for reading
f=open('practice.txt') # default read mode

# read entire data from file
text=f.read()

# print the content of the file
print(text)

f.close()

# another way to read a file
for l in open('practice.txt'):
    print(l)