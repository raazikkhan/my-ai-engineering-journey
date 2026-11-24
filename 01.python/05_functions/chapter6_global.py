# global keyword is used to modify a variable that belongs to the global scope. It allows you to assign a new value to a global variable from within a function, rather than creating a new local variable.

x = 10 # Global variable
def modify_global():
    global x # Declare x as global to modify it
    x = 20    # Modify the global variable
    print("Inside function, x:", x)

print("Before function call, x:", x)
modify_global()
print("After function call, x:", x)