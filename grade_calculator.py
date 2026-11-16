# Student Grade Calculator

students = {
    "Yash": 95,
    "Ali": 82,
    "Rahul": 74,
    "Aman": 61,
    "Rohit": 45
}

print("Student Grade Report")
print("-" * 30)

for name, marks in students.items():

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}: Marks = {marks}, Grade = {grade}")