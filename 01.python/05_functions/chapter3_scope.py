#Python follows the LEGB rule when looking up variable names, and searches for them in this order:
'''Local - Inside the current function
   Enclosing - Inside enclosing functions (from inner to outer)
   Global - At the top level of the module
   Built-in - In Python's built-in namespace
'''
def outer():
    outer_var = "I am outside!"
    def inner():
        inner_var = "I am Inside!"
        print(outer_var)  # Accessing outer variable
        print(inner_var)  # Accessing inner variable
    inner()
outer()  # Calling the outer function to execute the inner function    