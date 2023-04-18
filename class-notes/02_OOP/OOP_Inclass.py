import os
os.system('cls' if os.name == 'nt' else 'clear')

print("-------------------------------------")


def print_types(data):
    for i in data:
        print(i, type(i))
        
test=[122, "victor", ]


class Person:
    name="victor"
    age=18
    
person1= Person()
person2= Person()

print(person1.name)



















print("-------------------------------------")