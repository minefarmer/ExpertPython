# Python searches enclosing functions for referenced names.
# but never any enclosing classes
x=1

def nester():
    x=2
    print(x)  # 1
    class C:
        x=3
        print(x)  # 2
        def method1(self):
            print(x)  # 3  refer to the method not class
            print("%", +self.x)  # % 3
            print("*", +C.x)  # * 3
        def method2(self):
            x = 4
            print(x)
            self.x=5
            print(self.x)
    l=C()
    l.method1()
    l.method2()

print(x)
nester()
