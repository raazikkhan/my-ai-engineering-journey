#Numeric data types
#Python supports four different numerical types: int, boolean, float, and complex.
#Int: Integer, a whole number, positive or negative, without decimals, of unlimited length.
#Float: Float, or "floating point number" is a number, positive or negative, containing one or more decimals. Float can also be scientific numbers with an "e" to indicate the
#complex: Complex numbers are written with a "j" as the imaginary part, e.g., 2 + 3j. The real part is 2 and the imaginary part is 3j.
#boolean: Boolean value, either True or False. Used to represent truth values (logical values) of expressions.

#integer
bread_price = 17
milk_price = 3
#total_price = bread_price / milk_price  # classic division returns a float value
total_price = bread_price // milk_price  # floor division returns an integer value,the fractional part
total_price = bread_price % milk_price  # the % operator returns the remainder of the division
print(f"Total amount is {total_price}")
#float 
is_user_logged_in = True #upCasting
is_user_count  = 3
total_user_count = is_user_logged_in + is_user_count
print(f"User logging: {total_user_count}")
#float

tax = 12.5 / 100
price = 100.50
print(f"Tax amount is: {tax * price}")

#complex 
#is just like imaginary numbers in mathematics. It is written with a "j" as the imaginary part, e.g., 2 + 3j. The real part is 2 and the imaginary part is 3j.
complex_number = 2 + 3j
print(f"Complex number is: {complex_number}")