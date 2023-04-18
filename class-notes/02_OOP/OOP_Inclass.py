import os
os.system('cls' if os.name == 'nt' else 'clear')

print("-------------------------------------")

#!Topics to be Covered:

#* Everything in Python is class
#? Defining class
#* Defining class attributes
#? Difference between class attributes and instance attributes
#* SELF keyword
#? Static methods
#* Special methods (init, str)
#? 4 pillars of OOP:
#     Encapsulation
#     Abstraction
#     Inheritance
#        Multiple inheritance
#     Polymorphism
#        Overriding methods
#* Inner class


#! Everything in Python is class
# def print_types(data):
#     for i in data:
#         print(i, type(i))
        
        
# test = [122, "victor", [1,2,3], (1,2,3), {1,2,3}, True, lambda x:x]

# print_types(test)


#! Defining class & Defining class attributes


# class Person:
#     company = "clarusway"
    

# person1 = Person()
# person2 = Person()



# Person.job = "developer"
# print(person1.job)


#! Difference between class attributes and instance attributes

# person1.location = "Turkey"
# person1.name = "barry"
# person1.age = 18

# person2.name = "victor"
# person2.age = 35

# print(person1.location)

#! SELF keyword & Static methods

# class Person:
#     company = "clarusway"
    
#     def test(self):
#         print("test")
        
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age
        
#     def get_details(self):
#         print(self.name , self.age)
    
#     @staticmethod    
#     def salute():
#         print("Hi there!")
        
    
# person1 = Person()
# person2 = Person()

# # print(person1.company)
# person1.test()
# # Person.test(person1)

# person1.set_details("victor", 18)
# person2.set_details("barry", 20)

# # person2.get_details()
# person1.salute()
# person2.salute()

#! Special methods (init, str)

# class Person:
#     company = "clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def __str__(self):
#         return f"{self.name} - {self.age}"


# person1 = Person("victor", 18)
# person2 = Person("barry", 20)


# print(person1)


#! 4 pillars of OOP:
#     Encapsulation
#     Abstraction
#     Inheritance
#     Polymorphism


# class Person:
#     company = "clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._salary = 5000
#         self.__id = 2300
        
#     def __str__(self):
#         return f"{self.name} - {self.age}"
    

#     def get_details(self):
#         print(self.name , self.age)
    
# print(person1._salary)
# # print(person1.__id)
# print(person1._Person__id)

# class Language:
#     def __init__(self, lang):
#         self.lang = lang
    
#     def display_langs(self):
#         print(self.lang)

# class Employee(Person, Language):
    
#     def __init__(self, name, age, path, lang):
#         super().__init__(name, age)
#         # self.name = name
#         # self.age = age
#         self.path = path
#         # self.lang = lang
#         Language.__init__(self, lang)
        
#     def get_details(self):
#         Person.get_details(self)
#         Language.display_langs(self)
#         print(self.path)

# emp1 = Employee("victor", 18, "Fullstack", ["javascript", "python"])
# emp1.get_details()



# print(Employee.mro())
# print(help(Employee))
# print(emp1.__dict__)




# from django.db import models


# class Article(models.Model):
#     name = models.CharField(max_length=38)
#     author = models.CharField(max_length=40)
    
#     class Meta:
#         ordering= ['name',]
        
    



















print("-------------------------------------")


    

        
