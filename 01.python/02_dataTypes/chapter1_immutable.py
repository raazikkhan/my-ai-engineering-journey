sugar_amount = 10  # 'x' points to an integer object 10
print(f"sugar_amount {sugar_amount}")
sugar_amount = 20 # 'x' now points to a completely new integer object 20
print(f"sugar_amount {sugar_amount}") 
            # The object 10 remains unchanged in memory because its a IMmutable
            # In python we changing the reference not the actual value.
print(f"Id of 2: ", id(2))
#id(object) function returns a unique, constant integer representing the identity of a specified object during its lifetime
print(f"Id of 12: ", id(12))