#if/elif conditions

student_marks = int(input("Enter Your marks: "))
if student_marks >= 90:
    print(f"Your Grade is A")
elif student_marks >= 80:
    print(f"Your Grade is B") 
elif student_marks >= 70:   
    print(f"Your Grade is C")
else :
    print(f"Fail")        
#Boolean variables can be used directly in if statements without comparison operators.
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#If you have only one statement to execute, you can put it on the same line as the if statement.
x=10
y=20
if x < y: print("x is less than y")


