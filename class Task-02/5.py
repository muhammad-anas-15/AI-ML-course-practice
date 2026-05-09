import random

# Students list
students = ["Ali", "Sara", "Ahmed", "Fatima", "Usman"]

# Generate random attendance for 10 weeks
attendance = {}

for s in students:
    attendance[s] = [random.choice(["P", "A"]) for _ in range(10)]


# (a) Calculate attendance percentage
def attendance_percentage(record):
    present = record.count("P")
    total = len(record)
    return (present / total) * 100


# (d) Print formatted attendance report
print("========== ATTENDANCE REPORT ==========")

percentages = {}

for student, record in attendance.items():
    percent = attendance_percentage(record)
    percentages[student] = percent

    print(f"{student:<10} : {record}")
    print(f"Attendance: {percent:.2f}%")

    # (b) Short attendance warning
    if percent < 75:
        print("Status: SHORT ATTENDANCE WARNING!")
    else:
        print("Status: OK")

    print("----------------------------------------")


# (c) Week with lowest attendance
weeks = len(list(attendance.values())[0])
lowest_week = 0
lowest_present = len(students)

for i in range(weeks):
    present_count = 0
    for student in attendance:
        if attendance[student][i] == "P":
            present_count += 1

    if present_count < lowest_present:
        lowest_present = present_count
        lowest_week = i + 1

print("Week with lowest attendance:", lowest_week)


# Bonus: Prediction function
def predict_short_attendance(record):
    current_percent = attendance_percentage(record)
    if current_percent < 75:
        return "Likely to fall below 75%"
    else:
        return "Safe for now"


print("\n===== ATTENDANCE PREDICTION =====")
for student, record in attendance.items():
    print(student, "->", predict_short_attendance(record))