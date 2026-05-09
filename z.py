# str = ["Ali" , "Ahmed" , "Hamza"]
# dict = {name : len(name) for name in str}
# print(dict)    # Ali : 3 , Ahmed : 5 , "Hamza" : 5

#---------------------------------------------------------#



def receipt(o):
    prices = { 
        "chai" : 50,
        "paratha" : 40,
        "anda" : 30 
    }  

    subtotal = 0

    print("\n--------------------------\n")
    

    for item in o:
        quantity = o[item]
        item_total = prices[item] * quantity
        subtotal += item_total
        print(f"{item.capitalize()}  x{quantity}  Rs. {item_total}")

    print("\n--------------------------\n")

    discount = 0
    if subtotal > 500:
        discount = subtotal * 0.1

    subtotal -= discount   

    print(f"Subtotal:\t\t RS. {subtotal}")
    print(f"Discount (10%):\t\t RS.{discount}")
    print(f"Grand Total:\t\t RS. {subtotal}")

    print("\n--------------------------\n")

    print("Tip Suggestions:\n")
    print(f"{5}% -> Rs.{13.00}")
    print(f"{10}% -> Rs.{26.00}")
    print(f"{15}% -> Rs.{39.00}")


order = {"chai" : 3 , "paratha" : 2 , "anda" : 1}
receipt(order)

#---------------------------------------------------------#

students = [
    {
     "name" : "Ali", "roll number": "23P-0613",
     "gpa":[2.4 , 3.5 , 1.0 , 2.8, 0.7]  
    },
    {
     "name" : "Ahmed", "roll number": "23P-0713",
     "gpa":[2.4 , 3.5 , 3.0 , 2.8, 1.7]  
    },
    {
     "name" : "Abdullah", "roll number": "23P-0013",
     "gpa":[2.4 , 2.5 , 1.0 , 1.8, 0.7]  
    },
    {
     "name" : "Anas", "roll number": "23P-0913",
     "gpa":[2.4 , 0.5 , 1.0 , 3.8, 0.7]  
    },
    {
     "name" : "Akmal", "roll number": "23P-0513",
     "gpa":[3.9 , 3.9 , 3.0 , 3.8, 3.7]  
    },
]

for i in students:
    i["CGPA"] = sum(i["gpa"]) / len(i["gpa"])

sorted_students = sorted(students , key=lambda s: s["CGPA"] , reverse=True)

print("\n------------ All Students Sorted by CGPA -----------\n")

for s in sorted_students:
    print(f"{s['name']} ({s['roll number']}) -> CGPA: {s['CGPA']:.2f}")

print("\n------------ Students in Dean's list CGPA >=3.5 -----------\n")

for s in sorted_students:
    if s["CGPA"] >= 3.5:
        print(f"{s['name']} ({s['roll number']}) -> CGPA: {s['CGPA']:.2f}")
    
highest_GPA = sorted_students[0]
lowest_GPA = sorted_students[-1]

print("\n")

print("\n------------ Students with Highest GPA  -----------\n")
print(f"{highest_GPA['name']} ({highest_GPA['roll number']}) -> CGPA : {highest_GPA["CGPA"]:.2f}")

averge_CGPA = sum(s["CGPA"] for s in students) / len(students)

print("\n------ Avergae CGPA of Class ------\n\n")
print(f"{averge_CGPA:.2f}")

#---------------------------------------------------------#
import random

mains = ["chapli kabab", "namkeen gosht", "karahi", "shinwari tikka", "peshawari pulao"]
sides = ["raita","salad", "naan", "chutney"]
drinks = ["doodh patti", "green tea", "lassi", "sugarcane juice"]
deserts = ["firni", "jalebi", "kheer", "gulab jamun"]

# random combo meal
combo = {
    mains : random.choice(mains),
    sides : random.choice(sides),
    drinks : random.choice(drinks),
    deserts : random.choice(deserts)
}

# Party Platter

party_plater = {
    mains : random.choice(mains , 3),
    sides : random.choice(sides, 2),
    drinks : random.choice(drinks, 2),
    deserts : random.choice(deserts, 1)
}

def get_price(category):
    if category == "main":
        return random.int(300 , 800)
    elif category == "sides":
        return random.int(50 , 200)
    elif category == "drinks":
        return random.int(50 , 150)
    elif category == "deserts":
        return random.int(100 , 250)
    
#---------------------------------------------------------#

students = ["Ali" , "Hamza" , "Ahmed" , "Anas" , "Akmal"]
attendence = {}

for s in students:
    attendence[s] = [random.choice(["P" , "A"]) for _ in range(10)] 

def calculate_percentage(record):
    present = record.count("P")
    total = len(record)
    return (present / total) * 100

# student record with percentages

percentage = {}

for student , record in attendence.items:
    percent = calculate_percentage(record)
    percentage[student] = percent

    print(f"{student} : {record}")
    print(f"Attendence : {percent:.2f}")

    if percent < 75:
        print(f"Stort attendence warning")
    else:
        print(f"Safe!")
    
    print("---------------------------------------")

# Reading writing operations 

with open("file.txt" , "w") as f:
    f.write("Name , Roll , GPA\n")
    f.write("Anas , 0613 , 2.9\n")
    f.write("Ali , 0556 , 3.2\n")
    f.write("Ahmed , 0670 , 2.1\n")

with open("file.txt" , "r") as f:
    header = f.readline()
    for line in f:
        parts = line.strip().split(",")


with open("file.txt" , "r") as f:
    content = f.read()
    lines = f.readlines()
