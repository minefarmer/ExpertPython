class student():
    def s_name(self,name):
        self.name = name
    def s_age(self,age):
        self.age = age
    def qualification(self):
        return 'studying'
    def display(self):
        print("Name: ",self.name)
        print("age: ",self.age)
        print("Qualification: ",self.qualification())


class eng_student(student):
    def qualification(self):
        return 'engineering student'

bob = student()
bob.s_name("Bob")
bob.s_age(22)
bob.display()
            # Name:  Bob
            # age:  22
            # Qualification:  studying

mike = eng_student()
mike.s_name("Mike")
mike.s_age(21)
mike.display()
            # Name:  Mike
            # age:  21
            # Qualification:  engineering student