class Getter:
    def __init__(self, name):
        self.__name = name # private variable

    # getter method 
    # getter method is used to access the private variable from outside of the class.
    def get_name(self):
        return self.__name

get = Getter("razik")
# accessing private variable using getter method
data = get.get_name()    
print(data)


#__name is a private-style attribute.
#get_name() is the getter method.
# It returns the student's name.