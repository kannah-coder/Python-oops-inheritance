#1
"""
class twod:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def showvect(self):
        print(f"2D vector:{self.i}i+{self.j}j")
class threed(twod):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def showvect(self):
        print(f"3D vector:{self.i}i+{self.j}j+{self.k}k")
a=twod(2,3)
a.showvect()
b=threed(0,3,5)
b.showvect()

"""
from ast import increment_lineno
from numbers import Complex

#2
"""
class animals:
    def animals(self):
        print("we are animals")
class pets(animals):
    def pets(self):
        print("we are pets")
class dogs(pets):
    def dogs(self):
        print("we are dogs")
    def bark(self):
        print("we bark")

a=dogs()
a.animals()
a.pets()
a.dogs()
a.bark()

"""
#3
"""
class employee:
    salary=235
    increment=20
    @property
    def salaryinc(self):
        return self.salary + (self.salary * self.increment / 100)
    @salaryinc.setter
    def salaryinc(self,salary):
        self.increment= ((salary/self.salary)-1)*100


e=employee()
print(e.salaryinc)
e.salaryinc=282.0
print(e.increment)
"""
"""
class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,num):
        return complex(self.r+num.r,self.i+num.i)
    def __mul__(self,num):
        real_part = self.r * num.r - self.i * num.i  # ac - bd
        imag_part = self.r * num.i + self.i * num.r  # ad + bc
        return complex(real_part, imag_part)
    #as ouptut is not understanding use str
    def __str__(self):
        return f"{self.r}+{self.i}i"
c1=complex(2,3)
c2=complex(1,2)
print(c1+c2)
print(c1*c2)
"""
#5
"""
class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, num):
        return vector(self.x + num.x, self.y + num.y, self.z + num.z)

    def __mul__(self, num):
        # Dot product: x1*x2 + y1*y2 + z1*z2
        return self.x * num.x + self.y * num.y + self.z * num.z

    def __str__(self):
        return f"vector({self.x}, {self.y}, {self.z})"


# Example usage
v1 = vector(1, 2, 3)
v2 = vector(4, 5, 6)

print(v1 + v2)  # Output: vector(5, 7, 9)
print(v1 * v2)  # Output: 32 (dot product)
"""
# len
class vector:
    def __init__(self, l):
        self.l=l
    def __len__(self):
        return len(self.l)


# Example usage
v1 = vector([1, 2, 3])
print(len(v1))