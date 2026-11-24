# 1. Create a mutable list object
shopping_list = ["apples", "bananas", "cherries"]
print("Original List:", shopping_list)
print("Memory ID before:", id(shopping_list))

# 2. Modify an element in place
shopping_list[1] = "blueberries"

# 3. Add a new element
shopping_list.append("dates")

print("\nModified List:", shopping_list)
print("Memory ID after :", id(shopping_list))
