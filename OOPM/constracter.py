class employ:
    def __init__(self,name,age,salary):#ye constracter hai jo object bante hi call ho jata hai 
        self.name=name
        self.age=age
        self.salary=salary
    def get_info(self):
        print(f"Employ name is {self.name} and he is {self.age} year old his salary is {self.salary}")

e1=employ("gourav",19,1000000)
e2=employ("harsh",22,10000)
e3=employ("kariya",222,5000)

e1.get_info()
e2.get_info()
e3.get_info()