#*args and **kwargs let a function accept a variable number of arguments.
#Note: The names args and kwargs are just conventions. The * and ** are what matter. You could write *numbers or **options instead.
# note- *args collects multiple positional arguments into a tuple and how **kwargs collects keyword arguments into a dictionary.


# - *args collects extra positional arguments into a tuple.
def add_num(*args):
    print(args)
    return sum(args)
result = add_num(2,3,4)
print(result)

# example-2

def names(*names):
    for name in names:
        print(f"Hello {name}")
     
names("emi ", "harry", "jupiter")

# - **kwargs collects extra keyword arguments into a dictionary.

def person(**kwargs):
    print(kwargs)
    # You Can access like a normal dict.
    for key , value in kwargs.items():
        print(f"{key}: {value}")

person(name = "Razik", age = 25, state = "Bihar")       