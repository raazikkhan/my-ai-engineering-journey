# A recursive function is a function that calls itself.

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

"""
1. Built-in functions
       ↓
2. User-defined functions
       ↓
3. Parameters & arguments
       ↓
4. return
       ↓
5. Default arguments
       ↓
6. *args
       ↓
7. **kwargs
       ↓
8. Lambda functions
       ↓
9. Recursive functions
       ↓
10. Generator functions
       ↓
11. Methods + OOP

"""