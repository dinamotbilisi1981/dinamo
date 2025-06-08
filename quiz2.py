class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, sigrdze, sigane):
        self.sigrdze = sigrdze
        self.sigane = sigane
    
    def area(self):
        return self.sigrdze * self.sigane
    

class Dog:
    def speak(self):
        print("ძაღლიშვილი ვიყო")

class Cat:
    def speak(self):
        print("კატა ვარ")

cxovelebi = [Dog(), Cat()]

for animal in cxovelebi:
    animal.speak()


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def greet(self):
        print(f"chemi saxelia {self.firstname} {self.lastname} {self.age} years old.")

person1 = Person("dachi", "grdzelishvili", 15)
person2 = Person("sergo", "orjinikidze", 25)

person1.greet()
person2.greet()
