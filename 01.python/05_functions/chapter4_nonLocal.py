# the nonlocal keyword is used inside nested functions to modify a variable that belongs to an enclosing (outer) function's scope.
# its works just above the local scope but below the global scope. It allows you to assign a new value to a variable defined in an outer function, rather than creating a new local variable.

#Without nonLocal

def outer_function():
    count = 0
    def inner_function():
        count = 5  # Creates a new local variable; does NOT touch the outer count
        print("Inner count:", count)
        
    inner_function()
    print("Outer count:", count)

outer_function()

# With nonLocal keyword 

def outer_function():
    count = 0
    def inner_function():
        nonlocal count
        count = 5  # Modifies the outer variable
        print("Inner count:", count)
        
    inner_function()
    print("Outer count:", count)

outer_function()