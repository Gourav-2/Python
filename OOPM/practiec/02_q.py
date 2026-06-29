'''Create a class Person with a constructor ( __init__ ) that accepts name and age
as arguments and stores them as instance attributes.
Create an object and print the person’s name and age'''


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_info(self):
        print("name is",self.name,"age is ",self.age)

p1=person("nishant",55)
p1.get_info()