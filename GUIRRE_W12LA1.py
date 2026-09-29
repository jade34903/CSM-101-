student_name = input("Enter the name of the student: ")

class_record = {
    "S001": {
        "Name": "Jade",
        "Grades": [90, 59, 86, 82, 83, 90, 92]
    },
    "S002": {
        "Name": "Jeremy",
        "Grades": [72, 75, 69, 80, 84, 75, 85]
    },
}

found = False

for student_id, info in class_record.items():
    if info["Name"].lower() == student_name.lower():
        grades = info["Grades"]
        average_grade = sum(grades) / len(grades)
        lowest_grade = min(grades)
        highest_grade = max(grades)

        print(f"Student ID: {student_id}")
        print(f"Grades: {grades}")
        print(f"Average Grade: {average_grade:.2f}")
        print(f"Lowest Grade: {lowest_grade}")
        print(f"Highest Grade: {highest_grade}")

        for g in grades:
            if g < 60:
                print(f"{student_name} has a Grade below 60. Candidate for Intervention!")
                break

        found = True
        break

if not found:
    print("Student not found.")
