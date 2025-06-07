# Classes and Objects in Python
# Classes are blueprints for creating objects. They encapsulate data and behavior.
# Objects are instances of classes, representing specific data and functionality.


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         return "Woof!"


# my_dog = Dog("Buddy", 3)
# print(my_dog.name)  # Output: Buddy
# print(my_dog.age)  # Output: 3
# print(my_dog.bark())  # Output: Woof!


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


#     def moves(self):
#         print("The vehicle moves forward.")

#     def get_make_model(self):
#         print(f" I'm a {self.make} {self.model}")


# my_car = Vehicle("Toyota", "Corolla")
# my_car.moves()  # Output: The vehicle moves forward.
# my_car.get_make_model()  # Output: I'm a Toyota Corolla


# class Car(Vehicle):
#     def __init__(self, make, model, year):
#         super().__init__(make, model)
#         self.year = year

#     def get_year(self):
#         print(f"This car is from {self.year}.")


# my_sedan = Car("Honda", "Civic", 2020)
# my_sedan.moves()  # Output: The vehicle moves forward.
# my_sedan.get_make_model()  # Output: I'm a Honda Civic
# my_sedan.get_year()  # Output: This car is from 2020.

# Inheritance allows the Car class to inherit properties and methods from the Vehicle class, while also adding its own specific attributes and methods. This promotes code reuse and organization in object-oriented programming.


class Airplane(Vehicle):
    def moves(self):
        print("The airplane flies through the sky.")


class Truck(Vehicle):
    def moves(self):
        print("The truck drives on the road.")


class Motorcycle(Vehicle):
    pass


cessna = Airplane("Cessna", "172")
mack = Truck("Mack", "Anthem")
harley = Motorcycle("Harley-Davidson", "Street 750")

cessna.get_make_model()  # Output: I'm a Cessna 172
cessna.moves()  # Output: The airplane flies through the sky.
mack.get_make_model()  # Output: I'm a Mack Anthem
mack.moves()  # Output: The truck drives on the road.
harley.get_make_model()  # Output: I'm a Harley-Davidson Street 750
harley.moves()  # Output: The vehicle moves forward. (inherited from Vehicle)
# The Airplane, Truck, and Motorcycle classes inherit from the Vehicle class, allowing them to use its properties and methods while also defining their own specific behaviors. The Motorcycle class does not override the moves method, so it uses the default behavior from Vehicle.
# This demonstrates how inheritance allows for a flexible and organized structure in object-oriented programming, enabling the creation of specialized classes that build upon a common base class.
