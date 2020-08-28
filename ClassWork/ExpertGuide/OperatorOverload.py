class op_overloading:
    def __init__(self,number):
        self.number = number
    def __add__(self,other):
        # return op_overloading(self.number + other)
        return self.number * other
x = op_overloading(20)
y = x + 2
print(y)  # 40
