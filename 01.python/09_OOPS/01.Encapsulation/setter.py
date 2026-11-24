class Student:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
  # setter method 
  # setter method is used to set the value of the private variable from outside of the class.
    def set_name(self, new_name):
        self.__name = new_name


student = Student("Razik")

print(student.get_name())

student.set_name("Ahmed")

print(student.get_name())