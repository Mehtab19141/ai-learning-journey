#This is the first day of my coding and journey to ai development
#input and output
#comments
#variables
#Data Types
#Operations
#Random number
#=========================================================================================================================
import random
#First program
print("hello world")

#-----------------------------------------------------------

#single line comment
# print("hola;")

#Double line comment using (''' )
'''This is the multiline comment in the python'''

#------------------------------------------------------------
#Data types
#---------------------------
#integer
a = 55
print(a)
#---------------------------
#float
b = 44
print(b)
#---------------------------
#complex
c = 3j
print(c)
#--------------------------
#list
d = [1,2,3,4,5,6]
print(d)
#---------------------------
#Tuple
e = (1,2,3,4,5,6)
print(e)
#--------------------------
#dictionaries
f = {"name" : "mehtab ", "Age" : 33}
print(f)
#--------------------------
#set
g = {1,2,3,4,5,6}
print(g)
#-------------------------
#bool
h = True
print(h)
#------------------------
#range
i = range(10)
print(i)
print(list(i))
print(list(range(10)))

#Type()
#This is use to see the type of datatype and can be convert through datatypename():
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(g))
print(type(h))


#Global variable
#global variable can be accessed in and out of function
name = "mehtab"
def myfun():
    age = 44
    print(f"{name} is {age} years old")
myfun()

#Input Data From User
university_name = input("Please enter your university name: ")
print(f"{name} is studying in  {university_name} ")

#Random number
#their is no function in python to get random number but it is easy to get
num1 = random.randint(1,10)
print(num1)

#Operations are +, -, *, /, %
num1 = 22
num2 = 2
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print(num1 // num2)
