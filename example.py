"""

name="Ryan"
age=18
actual_age=18.3
print(name)
print(age)

print(type(name))
print(type(age))
math= (age + actual_age)* (age+actual_age)-age
print(math)

"""



"""
name=input("What is your name?")

def greet (x):
  print("hello",x)
  print("how do you do?")

greet(name)
"""

"""
def add_numbers(n1,n2):
        result=n1+n2
        return result
while  True:
    try:
        no= int(input("Enter a number: "))
        nt= int(input("Enter another number: "))
        print(add_numbers(no,nt))

        break
    except ValueError:
        print("please, enter valid values")


"""
"""
marks=[55,64,75,80,65]

def average_mark():
    total_mark=sum(marks)
    total_topics=len(marks)
    result=total_mark/total_topics
    return result
result=average_mark()

def final_grades():
    if result >= 80:
        grades= "A"
    elif result >=60:
        grades="B"
    elif result >= 50:
        grades= "C"
    else:
        grades="F"
    print(grades)

final_grades()
"""


"""


guess= input("enter a word (4 letters): ")
word= "Ryan"


###CHATGPT###

import secrets
import string
longitud_contrasena = int(input("Ingrese la longitud de la contraseña (por defecto 12): ") or 12)
caracteres = string.ascii_letters + string.digits + string.punctuation
contrasena_generada = ''.join(secrets.choice(caracteres) for _ in range(longitud_contrasena))
print("Contraseña generada:", contrasena_generada)