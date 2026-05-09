# -------- Base Class --------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# -------- Student Class --------
class Student(Person):
    def __init__(self, name, age, roll_number, gpa):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.gpa = gpa
        self.courses = []

    def enroll(self, course):
        if course.enroll_student(self):
            self.courses.append(course)

    def drop(self, course):
        if course.drop_student(self):
            if course in self.courses:
                self.courses.remove(course)


# -------- Instructor Class --------
class Instructor(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.courses_teaching = []


# -------- Course Class --------
class Course:
    def __init__(self, code, name, instructor, max_capacity=30):
        self.code = code
        self.name = name
        self.instructor = instructor
        self.max_capacity = max_capacity
        self.enrolled_students = []

    # enroll student
    def enroll_student(self, student):
        if len(self.enrolled_students) >= self.max_capacity:
            print(f"Cannot enroll {student.name}. Course {self.code} is full.")
            return False

        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print(f"{student.name} enrolled in {self.name}")
            return True

    # drop student
    def drop_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            print(f"{student.name} dropped from {self.name}")
            return True

    # display roster
    def display_roster(self):
        print(f"\nCourse: {self.name}")
        print("Students Enrolled:")
        for s in self.enrolled_students:
            print(f"{s.roll_number} - {s.name}")

    # average GPA
    def average_gpa(self):
        if len(self.enrolled_students) == 0:
            return 0
        total = sum(s.gpa for s in self.enrolled_students)
        return total / len(self.enrolled_students)


# -------- Create Instructor --------
instructor = Instructor("Dr. Ahmed", 45, "EMP101")

# -------- Create Courses --------
course1 = Course("CS101", "Programming Fundamentals", instructor)
course2 = Course("CS201", "Data Structures", instructor)
course3 = Course("CS301", "Operating Systems", instructor)

# -------- Create Students --------
s1 = Student("Ali", 20, "23K-001", 3.5)
s2 = Student("Sara", 21, "23K-002", 3.8)
s3 = Student("Usman", 20, "23K-003", 3.2)
s4 = Student("Hina", 22, "23K-004", 3.6)
s5 = Student("Zain", 21, "23K-005", 3.1)

# -------- Demonstrate Enrollment --------
s1.enroll(course1)
s2.enroll(course1)
s3.enroll(course1)
s4.enroll(course1)
s5.enroll(course1)

# Display roster
course1.display_roster()

# Average GPA
print("\nAverage GPA:", round(course1.average_gpa(), 2))

# -------- Drop Student --------
s3.drop(course1)

# Show roster again
course1.display_roster()

# -------- Try enrolling beyond capacity (simulate full course) --------
course_small = Course("CS999", "AI Seminar", instructor, max_capacity=2)

s1.enroll(course_small)
s2.enroll(course_small)
s3.enroll(course_small)  # should show full error