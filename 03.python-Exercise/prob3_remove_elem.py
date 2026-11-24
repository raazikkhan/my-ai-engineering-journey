# Remove Duplicate Element in a list 

numbers = [1,23,22,3,33,3,3,55,4,333,66,55,44,90,54,232,44,323,11,33,77,6545,33,66,88,99,77,88]

unique_elem  = []

for number in numbers:
    if number not in  unique_elem:
        unique_elem.append(number)
print(f"Unique Elements: {unique_elem}")        
