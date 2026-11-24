
#Example-1

def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup
total_bill = calculate_bill(10,20)
print(f"Your Total bill is {total_bill}")

#Example-2

#your shop add 10% vat on every order, you want this tb be consistence and traceable.
def add_vat(price , vat_rate):
    return price * (100 + vat_rate)/100

orders = [100, 230, 130, 170]
for items in orders:
    total_amount = add_vat(items, 10)
    print(f"Your total amount after adding vat is {total_amount}")