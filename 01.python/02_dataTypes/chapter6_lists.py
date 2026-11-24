#list is a mutable data type in Python. It is similar to a tuple, but it can be changed after it is created. Lists are defined using square brackets [] and can contain elements of different data types.
squares = [1,25,32,43,12]
print(f"squares list is {squares}")
squares.append(100) # adding an element to the end of the list
print(f"squares list after adding 100 is {squares}")
squares.remove(32) # removing an element from the list
squares.sort() # sorting the list in ascending order
print(f"squares list after removing 32 is {squares}")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f"letters list is {letters}")
letters[2:5] = ['Cat', 'Dog', 'Egg'] # replacing elements from index 2 to 4 with new elements
print(f"letters list after replacing elements from index 2 to 4 is {letters}")
letters[:] = [] # removing all elements from the list 
print(f"letters list after removing all elements is {len(letters)}") # length of the list is 0