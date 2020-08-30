# breaking out of multiple loop
class Exitloop(Exception):pass
try:
    while True:
        while True:
            for i in range(10):
                if i>3: raise Exitloop()  # 'break' exits just one level
                print('loop3',1)
            print('loop2')
        print('loop1')
except Exitloop:
    print('continuing......')  # continuing......
print('continued')  # continued


# loop3 1
# loop3 1
# loop3 1
# loop3 1
# continuing......
# continued
#  the loops are no as showen in the video