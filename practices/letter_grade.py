#ec 1st What is my grade

grade_percentage = float(input("what is your grade and percentage: "))

if grade_percentage < 60:
    print(f"your grade is an F {grade_percentage}")
elif grade_percentage >= 60 and grade_percentage < 64:
    print(f"your grade is a D-{grade_percentage}")
elif grade_percentage >= 64 and grade_percentage < 67:
    print(f"your grade is a D{grade_percentage}")
elif grade_percentage >= 67 and grade_percentage < 70:
    print(f"your grade is a D+{grade_percentage}")
elif grade_percentage >= 70 and grade_percentage < 75:
    print(f"your grade is a C-{grade_percentage}")
elif grade_percentage >= 75 and grade_percentage < 77:
    print(f"your grade is a C{grade_percentage}")
elif grade_percentage >= 77 and grade_percentage < 80:
    print(f"your grade is a C+{grade_percentage}")
elif grade_percentage >= 80 and grade_percentage < 84:
    print(f"your grade is a B-{grade_percentage}")
elif grade_percentage >= 84 and grade_percentage < 87:
    print(f"your grade is a B{grade_percentage}")
elif grade_percentage >= 87 and grade_percentage < 90:
    print(f"your grade is a B+{grade_percentage}")
elif grade_percentage >= 90 and grade_percentage < 94:
    print(f"your grade is a A-{grade_percentage}")
else:
    print(f"your grade is a A{grade_percentage}")
