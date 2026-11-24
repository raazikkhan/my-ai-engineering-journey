# Sets are used to store multiple items in a single variable.
# Set items are unchangeable, but you can remove items and add new items.
#Sets are written with curly brackets.
#Sets are unordered, so you cannot be sure in which order the items will appear.
# Set items are unordered, unchangeable, and do not allow duplicate values.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

mybooks = {"python for everyone", "python for data science", "python for machine learning"}
print(f"my all books {mybooks}")
#The values True and 1 are considered the same value in sets, and are treated as duplicates:
#The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2} 
print(f"{thisset}")

#frozenset is a set that is immutable, meaning that you cannot change its items after it has been created. You can create a frozenset by using the frozenset() function.
#Like sets, it contains unique, unordered, unchangeable elements.
#Unlike sets, elements cannot be added or removed from a frozenset.
myfrozenset = frozenset(["apple", "banana", "cherry"])
print(f"my frozenset is {myfrozenset}")