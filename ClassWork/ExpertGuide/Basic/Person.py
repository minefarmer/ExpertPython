class Person:
    def __init__(self,name,job=None,pay=9):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,per):
        self.pay = self.pay* (1+per)
    def __repr__(self):
        return '[Person:Name:%s Salary:%s]'%(self.name , self.pay)
class Manager(Person):
    def __init__ (self,name,pay):
        Person.__init__(self,name,'manager',pay)
    def giveRaise(self,per,bonus=.10):
        Person.giveRaise(self,per + bonus)
if __name__ =="__main__":
    
    bob=Person('Bob Mary','web developer',100000)
    michael=Person('michael ross')
    print(bob)
    print(michael)
    print(bob.lastName())
    print(michael.lastName())
    print(bob.pay)
    bob.giveRaise(.4)
    print(bob)
    tom=Manager("Tom Sayer",10000)
    print(tom)
    print(tom.job)
    tom.giveRaise(.10)
    print(tom)
    print(bob,michael)
    
# [Person:Name:Bob Mary Salary:100000]
# [Person:Name:michael ross Salary:9]
# Mary
# ross
# 100000
# [Person:Name:Bob Mary Salary:140000.0]
# [Person:Name:Tom Sayer Salary:10000]
# manager
# [Person:Name:Tom Sayer Salary:12000.0]
# [Person:Name:Bob Mary Salary:140000.0] [Person:Name:michael ross Salary:9]