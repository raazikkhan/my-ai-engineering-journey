# Count the number occurrence of a character into string

word = "Razik Khan"
character = 'i'

count = 0
for i in word:
    if i == character:
        print(character)
        count += 1
print(f"The Word is: {character} and count of number is: {count}")         