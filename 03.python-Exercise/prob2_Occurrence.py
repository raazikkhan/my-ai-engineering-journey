# Count Occurrences Of Element
items = ['apple', 'banana', 'coconut','apple','litchi', 123, 'kiwi']
target = 123
count = 0

for item in items:
    if item == target:
        count += 1
print(f"{target} appears: {count} Times")              