#Public data members are accessible within and outside of a class. All member variables of the class are by default public.

class cars:
    def __init__(self, name, color):


        #public data member 
        self.name = name 
        self.color = color
    #public date method
    def show(self):
        print(f"Car name is {self.name} and it's {self.color} color")   


       
#Creating a object
details = cars("bmw", "blue")



#Accessing Public data member 
print(f"{details.name} and color is {details.color}")

details.show()