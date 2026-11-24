#Dictionary is a collection of key value pairs.
#each key is unique and is used to access the corresponding value.
#Dictionaries are mutable, meaning that they can be changed after they are created.

user = {
    "name": "razik",
    "age": 25,
    "status": "A computer science student."
}
print(f"User Information {user}")

#Dictionary items are ordered, changeable, and do not allow duplicates.
print(f"User name is {user['name']}") #accessing value using key
user["age"] = 26 #changing value of a key
print(f"User Information after changing age {user}")


#The values in dictionary items can be of any data type:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(f"thisdict is {thisdict}")


#The keys() method will return a list of all the keys in the dictionary.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change