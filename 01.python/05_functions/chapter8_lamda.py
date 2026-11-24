# Lambda functions are commonly used with functions like map(), filter(), and sorted().
#a lambda function is a small, anonymous function that is defined without a name and contains exactly one expression

# example -2 
name = "razik khan"
upper = lambda x: x.upper()
print(upper(name))

check = lambda y: "positive" if y > 0 else "negative" if y < 0 else "zero"
print(check(2))
print(check(-2))
print(check(-33))