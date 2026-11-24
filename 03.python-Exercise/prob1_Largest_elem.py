# Find the Largest Element in a list.

Numbers  = [12,44,39,66,210,44,32]

Largest = Numbers[0]

for elem in Numbers[1:]:
    if elem > Largest:
        Largest = elem
print(Largest)
