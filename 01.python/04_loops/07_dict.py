users = { 
    1: {"total": 100, "coupon": "p20"}, 
    2: {"total": 200, "coupon": "p30"}, 
    3: {"total": 300, "coupon": "p40"} 
}

discounts = {
    "p20": (0.2,10),
    "p30": (0.3, 20),
    "p40":(0.4,30)
}

for user in users:
    percent, fixed = discounts.get(users[user]["coupon"], (0, 0))
    discounted_total = users[user]["total"] * (1 - percent) - fixed
    print(f"User {user} has a total of {users[user]['total']} and a coupon {users[user]['coupon']}. After discount, the total is {discounted_total}.")
