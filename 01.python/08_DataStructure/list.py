fruits = ["apple", "banana", "mango", "apple"]


constructorList = list(fruits)
print(constructorList)

print(fruits.append("orange"))

#list comprehension
inputList = [4,7,11,13,18,20]
#creating a list with square values of only the even numbers
squareList = [var**2 for var in inputList if var%2==0]
print(squareList)

#List Comprehension 
square = [x**2 for x in range(5)]
print(f"the square of 2 is : {square}")