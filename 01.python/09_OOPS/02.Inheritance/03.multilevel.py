#In multilevel inheritance, a class inherits from a child class or derived class. Suppose three classes A, B, C. A is the superclass, B is the child class # of A, C is the child class of B. In other words, we can say a chain of classes is called multilevel inheritance.

#base class
class Vehicle:
    def v_info(self):
        print("Inside vehicle class ")
#  child class
class Cars(Vehicle):
    def c_info(self):
        print("Inside car class")

# child class of Cars        
class SportCar(Cars):
    def s_info(self):
        print("inside sport car class")
    
s_car = SportCar()

s_car.v_info()
s_car.c_info()
s_car.s_info()


#Vehicle is the superclass, Car is a child of Vehicle, SportsCar is a child of Car. So we can see the chaining of classes.