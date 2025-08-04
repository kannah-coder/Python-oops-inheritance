"""
class employee:
    sec="g"   #class attribute
    salary=90000000
kannah=employee()
kannah.name="kannah" #object attribute or instance attribute
print(kannah.name,kannah.sec,kannah.salary)
"""
# here name is  instance attribute and salry and sec is are class attributes as they are directly belong to class
# precendece of instance attribute is higherr than class attribute


"""
class employee:
    sec="g"   #class attribute
    salary=90000000
    def getinfo(self):
        print(f"the section is {self.sec} the salary is {self.salary} ")
    @staticmethod
    def greet():
        print("good night")
kannah=employee()
kannah.name="kannah" #object attribute or instance attribute
print(kannah.name,kannah.sec,kannah.salary)
kannah.getinfo() #employee.getinfo(kannah)
kannah.greet()
"""
"""
#employee.getinfo(kannah)
class employee:
    sec="g"   #class attribute
    salary=90000000
    def __init__(self): # dunder method which is automatically callled
        print("iam back")
    def getinfo(self):
        print(f"the section is {self.sec} the salary is {self.salary} ")
    @staticmethod
    def greet():
        print("good night")
kannah=employee()
kannah.name="kannah" #object attribute or instance attribute
print(kannah.name,kannah.sec,kannah.salary)
kannah.getinfo()
kannah.greet()
"""

class employee:
    sec="g"   #class attribute
    salary=90000000
    friend="karthik"
    def __init__(self,name,sec,salary):# dunder method which is automatically callled
        self.name=name
        self.sec=sec
        self.salary=salary

    def getinfo(self):
        print(f"the section is {self.sec} the salary is {self.salary} ")
    @staticmethod
    def greet():
        print("good night")
kannah=employee("kannah","A",1900000000)
print(kannah.name,kannah.salary,kannah.sec,kannah.friend)

