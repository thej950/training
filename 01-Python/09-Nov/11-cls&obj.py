# person_class.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object and call the method
person1 = Person("Navathej", 25)
person1.greet()
