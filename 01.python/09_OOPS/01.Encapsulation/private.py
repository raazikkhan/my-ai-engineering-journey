class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public attribute
        self.__salary = salary  # Private attribute

data = Employee("razik", 12)   
# print(data.name, data.__salary) # AttributeError: 'Employee' object has no attribute '__salary'

#We can access private members from outside of a class using the following two approaches
# Create public method to access private members
# Use name mangling


# Access Private member outside of a class using an instance method
class Employee1:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

# creating object of a class
emp = Employee1('Jessa', 10000)

# calling public method of the class
emp.show()

#The name mangling is created on an identifier by adding two leading underscores and one trailing underscore, like this _classname__dataMember, where  # classname is the current class, and data member is the private variable name.
#Example3 
class Employee3:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee3('Jessa', 10000)

print('Name:', emp.name)
# direct access to private member using name mangling
print('Salary:', emp._Employee3__salary)
