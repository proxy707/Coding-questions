class Employee:
    leaves=8
    def __init__(self,aname, asalary):
        self.name=aname
        self.salary=asalary
    def printdetails(self):
        print(f"(Print details)name is {self.name} salary is {self.salary}")

    def __add__(self,other):# Special method known as Dunder add : it is helping us to manage operator overloading
        return self.salary+other.salary
    
    def __truediv__(self,other):
        return self.salary/other.salary

    def __repr__(self):
        return f"(repr)Employee ('{self.name}'),{self.salary}"
    
    def __str__(self):#even if we do not define and explicitly call str then repr will be printed and if it is present then it will overwrite repr, repr will only be printed when called explicitly
        return f"(str)Employee Name is ('{self.name}'),Salary is {self.salary}"
        
emp1=Employee("Harry",1000)
emp2=Employee("Larry",200)
emp2.printdetails()
print(emp1+emp2) #It would cause error without __add__ as it will get confuse what is to be added
print(emp1/emp2)
print(emp1)#__str__ is being used even when it is not called
print(repr(emp1))
print(str(emp1))

"""
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in
__call__ for calling objects as functions,
 __int__, __str__, and the like, for converting objects to built-in types.
"""