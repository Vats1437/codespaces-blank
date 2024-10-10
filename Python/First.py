# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")


# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")


# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")
  
# if a > b: print("a is greater than b")

# a = 2
# b = 330
# print("A") if a > b else print("B")


# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")

# i = 1
# while i <= 10:
#   print(i*2)
#   i += 1
  
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
  
# for x in "banana":
#   print(x)
  
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)
  

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)
  
# for x in range(6):
#   print(x)

# for x in range(2, 6):
#   print(x)

# for x in range(2, 30, 3):
#   print(x)
  
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)


# for x in [0, 1, 2]:
#   pass


# def my_function():
#   print("Hello from a function")
  
# my_function()

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")


# class Parent:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f"Parent Init: {self.name}, {self.age}")

# class Child(Parent):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)  # Calls Parent's __init__ with any arguments passed
#         # print("Child Init")

# # Example usage
# child = Child("John", 12)


# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()


# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)


# import sys

# print(sys.version)

# if 5 > 2:
#  print("Five is greater than two!") 
# if 5 > 2:
#  print("Five is greater than two!") 
 

# Get the Type
# You can get the data type of a variable with the type() function.

# Example
# x = 5
# y = "John"
# print(type(x))
# print(type(y))



# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

# Example

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)


# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

# Example

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

# Example
# Unpack a list:

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)


# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)


# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)


# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

# Example
# Create an f-string:

# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)


# price = 59
# txt = f"The price is {price} dollars"
# print(txt)


# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# print(key.decode())

for i in range(5):
    print(i)
