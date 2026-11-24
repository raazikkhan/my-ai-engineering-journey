#string is immutable, once created it cannot be changed. Any operation on string will create a new string object.
customer_name = "Razik"
item = "garlic bread and diet coke"
print(f"Order for {customer_name} : {item} please ! ")

order_description = "one coke and two garlic breads"
print(f"First word in order description is: {order_description[0]}") #accessing first word of string
print(f"First word in order description is: {order_description[:8]}") #context: [:8] is used to access a substring from the beginning to index 8
print(f"First word in order description is: {order_description[12:20]}") #context: [12:20] is used to access a substring from index 12 to 20
print(f"First word in order description is: {order_description[::-1]}") #context: [::-1] is used to reverse the string. It means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.

#converting spacial characters to string
special_characters = "Hello, World! @#$%^&*()_+"
encoded_label = special_characters.encode("utf-8")
print(f"Encoded label: {encoded_label}")

print(r'C:\this\name')  # here \t means tab, \n means newline

#If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote.
