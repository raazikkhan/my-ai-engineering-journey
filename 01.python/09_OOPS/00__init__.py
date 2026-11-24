#Example-1

class Student:

    #__init__ is a special method that is automatically called when a object created.
    def __init__(self,name, age):
    
        self.name = name
        self.age = age

    #self  refer to the current class it helps to access the instance variable and method.

    def display(self):
        print(self.name,self.age)    
#creating a object
Student1 = Student("razik", 25)
Student1.display()        


#Example - 2 

class Animal:

    def __init__(self,name, category, age):
        self.name = name
        self.category = category
        self.age = age

    def displayAnimals(self):
        print(f"Name: {self.name}", f"Category: {self.category}", f"Age: {self.age}")     

All_Animals = Animal("Dog", "pet", 3)
All_Animals.displayAnimals()


#Example - 3
class Employee:
    # class variables
    company_name = 'ABC Company'

    # constructor to initialize the object
    def __init__(self, name, salary):
        # instance variables
        self.name = name
        self.salary = salary

    # instance method
    def show(self):
        print('Employee:', self.name, self.salary, self.company_name)

# create first object
emp1 = Employee("Harry", 12000)
emp1.show()

# create second object
emp2 = Employee("Emma", 10000)
emp2.show()

        
