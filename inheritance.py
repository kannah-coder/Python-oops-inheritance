#inheritance is a way of creating a new class form an existing class
"""
#syntax:
class employee:
    #codde
class programmer(employee): # derived or child class
    #code
"""
"""
TYPES OF INHERITANCE:
*SINGLE
*MULTIPLE
*MULTILEVEL
"""
#single you know
#multiple inhertance:
"""
# First base class
class Father:
    def skills(self):
        print("Father: Knows gardening and carpentry.")

# Second base class
class Mother:
    def skills(self):
        print("Mother: Knows cooking and painting.")

# Derived class inherits from both Father and Mother
class Child(Father, Mother):
    def skills(self):
        print("Child:")
        Father.skills(self)   # Call Father's method
        Mother.skills(self)   # Call Mother's method

# Create object of Child
c = Child()
c.skills()
"""
# multilevel inheritance
"""
# Base class
class Animal:
    def speak(self):
        print("Animal speaks")

# Derived class 1 (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Derived class 2 (inherits from Dog)
class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

# Create an object of the most derived class
p = Puppy()

# Call methods from all levels
p.speak()   # From Animal
p.bark()    # From Dog
p.weep()    # From Puppy

"""
"""

#super() method
# it is used to access the methods of super class in the derived class

class Animal:
    def __init__(self):
        print("constructor of animal")
    def speak(self):
        print("Animal speaks")

# Derived class 1 (inherits from Animal)
class Dog(Animal):
    def __init__(self):
        print("constructor of dog ")
    def bark(self):
        print("Dog barks")

# Derived class 2 (inherits from Dog)
class Puppy(Dog):
    def __init__(self):

        super().__init__()

        print("constructor of puppy")
    def weep(self):
        print("Puppy weeps")

# Create an object of the most derived class
p = Puppy()

# Call methods from all levels
p.speak()   # From Animal
p.bark()    # From Dog
p.weep()    # From Puppy
"""

"""
# class methods

class employees:
    a=1
    @classmethod  # it shows class attribute value over insatance attribute 
    def show(cls):
        print(f'the class attribute of a is {cls.a}')
e=employees()
e.a=45
e.show()

"""
"""
#property decorators
class employees:
    a=1
    @classmethod
    def show(cls):
        print(f'the class attribute of a is {cls.a}')
    @property
    def name(self):
        return f"{self.fname}{self.lname}"
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
e=employees()
e.a=45

e.name="rohith kannah"
print(e.name)
print(e.fname,e.lname)
e.show()
"""
#operations methods
class number:
    def __init__(self,n):
        self.n=n
    def __add__(self, num):
        return self.n+num.n
r=number(5)
m=number(40)
print(r+m)
#p1.__sub__(p2):
#p1.__mul__(p2):
#p1.__truediv__(p2):
#p1.__floordiv__(p2):
#__len__()  = used to set what displayed upon calling .__len__() or len(obj)
#str__() = used to set what gets displayed upon calling str(obj)







 



