# CGPA Analyzer

students = [
    {"name": "Ali", "roll": "22P-0001",
     "gpas": [3.7, 3.5, 3.8, 3.6, 3.9]},

    {"name": "Sara", "roll": "23P-0002",
     "gpas": [3.9, 4.0, 3.7, 3.8, 3.9]},

    {"name": "Ahmed", "roll": "25P-0003",
     "gpas": [3.2, 3.0, 3.4, 3.1, 3.3]},

    {"name": "Noor", "roll": "20P-0004",
     "gpas": [3.6, 3.7, 3.8, 3.5, 3.6]},

    {"name": "Usman Tariq", "roll": "24P-0005",
     "gpas": [2.9, 3.1, 3.0, 3.2, 3.0]}
]

# Calculate CGPA for each student
for student in students:
    student["cgpa"] = sum(student["gpas"]) / len(student["gpas"])

# (a) Sort students by CGPA (highest first)
sorted_students = sorted(students, key=lambda s: s["cgpa"], reverse=True)

print("===== Students Sorted by CGPA =====")
for s in sorted_students:
    print(f"{s['name']} ({s['roll']}) -> CGPA: {s['cgpa']:.2f}")

# (b) Dean's List (CGPA >= 3.5)
print("\n===== Dean's List (CGPA >= 3.5) =====")
for s in sorted_students:
    if s["cgpa"] >= 3.5:
        print(f"{s['name']} -> CGPA: {s['cgpa']:.2f}")

# (c) Highest and Lowest CGPA
highest = sorted_students[0]
lowest = sorted_students[-1]

print("\n===== Highest CGPA =====")
print(f"{highest['name']} -> {highest['cgpa']:.2f}")

print("\n===== Lowest CGPA =====")
print(f"{lowest['name']} -> {lowest['cgpa']:.2f}")

# (d) Class Average CGPA
class_average = sum(s["cgpa"] for s in students) / len(students)

print("\n===== Class Average CGPA =====")
print(f"{class_average:.2f}")