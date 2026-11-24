# Python also provides a more Pythonic way to implement getters and setters using @property.
class Student:
 #We use getters and setters as part of encapsulation to provide controlled access to data. We can also use the @property decorator to implement them in a more Pythonic way."
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name:
            self.__name = new_name


student = Student("Razik")

# Getter
print(student.name)

# Setter
student.name = "Ahmed"

print(student.name)