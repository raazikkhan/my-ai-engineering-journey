try:
    a = int(input("Enter your first value: "))
    b = int(input("Enter your Second value: "))
    print("What Kind of Operation you want to performed (+, -, *, /)")
    output = input("PLease Enter your Operation: ")

    match output:
        case '+':
            print(f"Addition of a and b is: {a + b}: ") 
        case '-':
            print(f"Subtraction of a  and b is: {a - b}: ")      
        case '*':
            print(f"Multiply of a  and b is: {a * b}: ")      
        case '/':
            print(f"Division of a  and b is: {a / b}: ")      
        case _:
            print("There is an Error...")    

except Exception as e:
    print("There is an Error: ", e)