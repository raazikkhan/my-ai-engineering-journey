#Tuple is a immutable data type in Python. It is similar to a list, but it cannot be changed after it is created. Tuples are defined using parentheses () and can contain elements of different data types.

#Creating a tuple

fruits = ("Apple", "Banana", "Pineapple")
(bucket1, bucket2, bucket3) = fruits # Unpacking the tuple into individual variables
print(f"bucket 1 is {bucket1}, bucket 2 is {bucket2}, bucket 3 is {bucket3}")

#assigning values to multiple variables using tuple unpacking
ginger, onion =  1,2 
print(f"ginger is {ginger}, onion is {onion}")

#Swapping the values of ginger and onion using tuple unpacking
#easy way to swap values in Python without using a temporary variable
ginger, onion = onion, ginger
print(f"ginger is {ginger}, onion is {onion}")

#membership operator
print("Apple" in fruits) # True