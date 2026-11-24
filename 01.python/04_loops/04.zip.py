# zip is a built-in function in Python that allows you to combine multiple iterables (like lists or tuples) into a single iterable of tuples. Each tuple contains elements from the input iterables that are at the same index.
names = ["mohammad", "razik", "khan"]
bills = 43, 65, 32
for name, amount in zip(names, bills):
    print(f"{name} paid for {amount}")