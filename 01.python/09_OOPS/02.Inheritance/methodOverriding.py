# Method overriding happens when a child class defines its owns versions of method that is already define in its parent class.


class Student:
    def student_info(self):
        print("this is a parent class")

class marks(Student):
    def student_info(self):
        print("this is a child class overrides a parent class")

stud = marks() 
stud.student_info()    

# example 2
# The super function returns a temporary object of the parent class that allows us to call a parent class method inside a child class method.
#super() allows a child class to call a method from its parent class.
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


dog = Dog()
dog.sound()