class Employee:
    #constructor 
    def __init__(self, name, salary, project):
        # Data members 
        self.name = name
        self.salary = salary
        self.project = project

    #Method
    def show(self):
        print(f"{self.name} and his salary is {self.salary}")    

    #Methods 
    def work(self):
        #Access public data member 
        print(f"{self.name} Working on {self.project}")   

#creating objects 
emply = Employee("razik", '12Lpa', 'Ai/Ml')     

#calling public methods from the class 
emply.show()
emply.work()