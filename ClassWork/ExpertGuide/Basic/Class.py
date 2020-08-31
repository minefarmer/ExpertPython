# make class
# class my_class:
#     def a(self):
#         print("Welcome to first python class")

# # making instance of class
# class_obj = my_class()
# class_obj.a();

class a_class():
    # data member
    a_data = 20
    
    # method
    def method_class(self):
        self.a_data = 40
        


# making object
an_obj = a_class()

print(an_obj.a_data)  # 20

# calling method object_name.method_name
an_obj.method_class()
# method_class(an_obj)

# printing instance variable
print(an_obj.a_data)  # 40

# printing class variable
print(a_class.a_data)  # 20

an_obj.name = 'abc'
print(an_obj.name)  # abc

an_obj.class1 = "12th"
print(an_obj.class1)  # 12th

