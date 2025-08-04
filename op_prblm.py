"""
class programmer:
    company="microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
p=programmer("harry",1900000,123123)
print(p.name,p.salary,p.pin)
r=programmer("kannah",2500000000,143143)
print(r.name,r.salary,r.pin)
"""
"""
class calculator:
    def __init__(self,n):
        self.n=n
    def new(self):
        print(f'squre of its:{self.n**2}')
        print(f'its cube:{self.n**3}')
p=calculator(5)
print(f'it is {p.n}')
p.new()
"""
"""
class demo:
    a=5
object=demo()
object.a=0

print(object.a)
print(demo.a) # so class attribute not changes as instant attributes not changes
"""
#4
"""
class calculator:
    def __init__(self,n):
        self.n=n
    def new(self):
        print("SQUARE is :",self.n**2)
        print("CUBE is:",self.n**3)
    def hello():
        print("HELLO BROH")    
a=calculator(5)
a.hello()
print(f"it is {a.n}")
a.new()
"""
#5
from random import randint
class train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"ticket is book in train no:{self.trainNo} from {fro} to {to}")
    def getstatus(self):
        print(f'train no {self.trainNo} is running succesfully')
    def getfare(self,fro,to):
        print(f"ticket fare in train no :{self.trainNo} from {fro} to {to} is {randint(222,666)}")
t=train(123456)
t.book("rampur","delhi")
t.getstatus()
t.getfare("rampur","delhi")





