from student.student import student
from student.utils import calculate_grades

student1 = student("Razik", 20)
student1.display()

grade = calculate_grades(85)
print(f"Grade: {grade}")