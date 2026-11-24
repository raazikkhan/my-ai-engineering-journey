# Counting Consonents  into in a given words 

vowel = ['a','e','i', 'o','u']
word = 'programming'

count = 0

for constant in word:
    if constant not in vowel:
        count += 1
print(count)        