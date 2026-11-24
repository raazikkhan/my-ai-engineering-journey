# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruit  = ["apple", "banana", "cherry"]
for x in fruit:
     print(x, len(x))

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status     

        print(active_users)
        