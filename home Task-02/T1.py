# FAST NUCES Transcript Generator

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
dept = input("Enter Department: ")
semester = input("Enter Semester: ")

courses = []
credits = []
marks = []

# Input for 6 courses
for i in range(6):
    print(f"\nEnter details for Course {i+1}")
    course_name = input("Course Name: ")
    credit_hour = int(input("Credit Hours (1-4): "))
    mark = int(input("Marks (0-100): "))

    courses.append(course_name)
    credits.append(credit_hour)
    marks.append(mark)

# Function to convert marks to grade
def get_grade(m):
    if m >= 90:
        return "A", 4.0
    elif m >= 85:
        return "A-", 3.67
    elif m >= 80:
        return "B+", 3.33
    elif m >= 75:
        return "B", 3.0
    elif m >= 70:
        return "B-", 2.67
    elif m >= 65:
        return "C+", 2.33
    elif m >= 60:
        return "C", 2.0
    elif m >= 50:
        return "D", 1.0
    else:
        return "F", 0.0

print("\n")
print(f"{'Fast Nuces Transcript Generator'}")
print("========================================")

print(f"Name: {name}")
print(f"Roll No: {roll}")
print(f"Department: {dept}")
print(f"Semester: {semester}")

print("------------------------------------------------------")
print(f"{'Course':<20}{'Cr':<5}{'Marks':<8}{'Grade':<8}{'GPA':<5}")
print("------------------------------------------------------")

total_points = 0
total_credits = 0

for i in range(6):
    grade, gpa = get_grade(marks[i])

     # Total points for GPA calculation
    total_points += gpa * credits[i]
    total_credits += credits[i]

    print(f"{courses[i]:<20}{credits[i]:<5}{marks[i]:<8}{grade:<8}{gpa:<5}")

semester_gpa = total_points / total_credits

print("------------------------------------------------------")
print(f"{'Semester GPA':<45}{semester_gpa:.2f}")
print("------------------------------------------------------")