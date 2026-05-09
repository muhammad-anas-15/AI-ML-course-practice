import csv

filename = "students.csv"

# -------- (a) Create CSV with 20 students --------
def create_file():
    students = [
        ["Ali","23K001","CS",3,3.2],
        ["Sara","23K002","AI",2,3.5],
        ["Usman","23K003","SE",4,2.8],
        ["Hina","23K004","CS",1,3.7],
        ["Zain","23K005","DS",5,1.9],
        ["Ayesha","23K006","CS",2,3.0],
        ["Hamza","23K007","SE",3,2.5],
        ["Fatima","23K008","AI",4,3.9],
        ["Bilal","23K009","DS",1,2.1],
        ["Kiran","23K010","CS",2,3.4],
        ["Omar","23K011","SE",3,2.2],
        ["Noor","23K012","AI",4,3.1],
        ["Ahmed","23K013","CS",1,1.8],
        ["Sana","23K014","DS",5,2.7],
        ["Raza","23K015","SE",6,3.6],
        ["Maha","23K016","AI",3,3.3],
        ["Daniyal","23K017","CS",2,2.4],
        ["Iqra","23K018","DS",4,3.8],
        ["Saad","23K019","SE",5,1.7],
        ["Laiba","23K020","CS",1,3.9]
    ]

    with open(filename,"w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name","Roll","Department","Semester","CGPA"])
        writer.writerows(students)

    print("CSV file created with 20 students.")


# -------- (b) Display all students --------
def display_students():
    with open(filename,"r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


# -------- (c) Search by roll number --------
def search_student():
    roll = input("Enter Roll Number: ")

    with open(filename,"r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1] == roll:
                print("Student Found:",row)
                return
    print("Student not found.")


# -------- (d) Update CGPA --------
def update_cgpa():
    roll = input("Enter Roll Number: ")
    new_cgpa = input("Enter new CGPA: ")

    rows = []

    with open(filename,"r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    for row in rows:
        if row[1] == roll:
            row[4] = new_cgpa
            print("CGPA updated.")

    with open(filename,"w",newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


# -------- (e) Delete student --------
def delete_student():
    roll = input("Enter Roll Number to delete: ")

    rows = []

    with open(filename,"r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    new_rows = [rows[0]]

    for row in rows[1:]:
        if row[1] != roll:
            new_rows.append(row)

    with open(filename,"w",newline="") as f:
        writer = csv.writer(f)
        writer.writerows(new_rows)

    print("Student deleted if existed.")


# -------- (f) Summary report --------
def summary_report():
    with open(filename,"r") as f:
        reader = csv.DictReader(f)
        students = list(reader)

    total = len(students)

    cgpas = [float(s["CGPA"]) for s in students]
    avg = sum(cgpas)/total

    dept_count = {}
    probation = []

    for s in students:
        dept = s["Department"]
        dept_count[dept] = dept_count.get(dept,0) + 1

        if float(s["CGPA"]) < 2.0:
            probation.append(s["Name"])

    print("\nTotal Students:",total)
    print("Average CGPA:",round(avg,2))
    print("Department Count:",dept_count)
    print("Students on Probation:",probation)


# -------- Menu --------
while True:

    print("\nStudent Database Manager")
    print("1. Create CSV File")
    print("2. Display Students")
    print("3. Search by Roll")
    print("4. Update CGPA")
    print("5. Delete Student")
    print("6. Summary Report")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_file()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_cgpa()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        summary_report()

    elif choice == "7":
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")