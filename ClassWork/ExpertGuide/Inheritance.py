class first:
    def setdata(self,value):
        self.data = value
    def getdata(self):
        print('class first',self.data)  # class first 50
obj = first()
obj.setdata(50)
obj.getdata()  # class first 50

# inheritance
class second(first):
    # overriding
    def getdata(self):
        print('SECOND CLASS:',self.data)  # SECOND CLASS: hi
    # adding more attributes
    def message(self):
        print('inheritance is an oop concept')  # inheritance is an oop concept
        
x = first()
x.setdata(2)
x.getdata()

y = second()
# inheriting method of base class
y.setdata('hi')
y.getdata()
y.message()
# x still belongs to first class
x.getdata()
