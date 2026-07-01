class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    
    def get_info(self):
        print(f"student name is {self.name} and he is {self.age} year old")
    
    @staticmethod
    def sum(a,b):
        print(a+b)

s1=student("nitin",23)
s1.get_info()

s1.sum(2,5)
        