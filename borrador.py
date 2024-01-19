"""
class student:
    pass
student1= student()
student1.name= "Harry"
student1.marks=85 
print(student1.name)
print(student1.marks)

class Student:
    def check_pass_fail(self):
        if self.marks >=40:
            return True
        else:
            return False
student1= Student ()
student1.name = 'Harry'
student1.marks=85

did_pass= student1.check_pass_fail()
print(did_pass)
"""

"""
 
class student:
    def check_pass_fail(self):
        if self.marks >=60:
            return True
        else:
            return False
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
student1= student("Harry",85)
student2=student("Ana", 45)
did_pass=student1.check_pass_fail()
print(student1.name,student1.marks,did_pass)
did_pass=student2.check_pass_fail()
print(student2.name,student2.marks,did_pass)


"""
class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def add(self,number):
        real=self.real+number.real
        imag=self.imag + number.imag
        result=complex(real,imag)
        return result
n1=complex(5,6)
n2=complex(-4,2)
result=n1.add(n2)
print("real=",result.real)
print("imag=",result.imag)

