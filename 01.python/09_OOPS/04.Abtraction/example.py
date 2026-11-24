from abc import ABC, abstractmethod

# ABC is used to create an abstract base class.
# @abstractmethod defines a method that subclasses must implement.
# Car provides its own implementation of start()




class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car is starting")    

car = Car()
car.start()        