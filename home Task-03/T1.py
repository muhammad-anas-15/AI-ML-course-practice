import json
import random

# Book Class 
class Book:
    def __init__(self, isbn, title, author, quantity):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.quantity = quantity
        self.available_quantity = quantity


# Member Class 
class Member:
    def __init__(self, mid, name):
        self.id = mid
        self.name = name
        self.borrowed_books = []
        self.max_books = 3


# Library Class 
class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}

# Add Book
    def add_book(self):
        isbn = input("ISBN: ")
        title = input("Title: ")
        author = input("Author: ")
        qty = int(input("Quantity: "))
        self.books[isbn] = Book(isbn,title,author,qty)

        print("Book added.")

# Remove Book
    def remove_book(self):
        isbn = input("Enter ISBN: ")

        if isbn in self.books:
            del self.books[isbn]
            print("Book removed.")

        else:
            print("Book not found.")

# Register Member
    def register_member(self):
        mid = input("Member ID: ")
        name = input("Name: ")
        self.members[mid] = Member(mid,name)

        print("Member registered.")

# Remove Member
    def remove_member(self):
        mid = input("Member ID: ")

        if mid in self.members:
            del self.members[mid]
            print("Member removed.")

        else:
            print("Member not found.")

# Borrow Book
    def borrow_book(self):
        mid = input("Member ID: ")
        isbn = input("ISBN: ")

        if mid not in self.members:
            print("Member not found.")
            return

        if isbn not in self.books:
            print("Book not found.")
            return

        member = self.members[mid]
        book = self.books[isbn]

        if len(member.borrowed_books) >= member.max_books:
            print("Borrow limit reached.")
            return

        if book.available_quantity <= 0:
            print("Book not available.")
            return

        member.borrowed_books.append({
            "isbn": isbn,
            "days": random.randint(1,30)   # simulate borrow days
        })

        book.available_quantity -= 1
        print("Book borrowed successfully.")

# Return Book
    def return_book(self):
        mid = input("Member ID: ")
        isbn = input("ISBN: ")

        if mid not in self.members:
            print("Member not found.")
            return

        member = self.members[mid]

        for b in member.borrowed_books:
            if b["isbn"] == isbn:
                member.borrowed_books.remove(b)
                self.books[isbn].available_quantity += 1

                print("Book returned.")
                return

        print("Book not found in member record.")

# Search Book
    def search_book(self):
        keyword = input("Enter title/author keyword: ").lower()

        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                print(book.isbn, book.title, book.author, "Available:", book.available_quantity)

# Overdue Simulation
    def overdue_books(self):
        print("Overdue Books (>14 days):")

        for member in self.members.values():
            for b in member.borrowed_books:
                if b["days"] > 14:
                    book = self.books[b["isbn"]]
                    print(member.name,"->",book.title,"(",b["days"],"days )")

# Save to JSON
    def save(self):

        data = {}
        data["books"] = {}
        data["members"] = {}

    # Save books
        for isbn in self.books:
            book = self.books[isbn]

            data["books"][isbn] = {
                "isbn": book.isbn,
                "title": book.title,
                "author": book.author,
                "quantity": book.quantity,
                "available_quantity": book.available_quantity
            }

    # Save members
        for mid in self.members:
            member = self.members[mid]

            data["members"][mid] = {
                "id": member.id,
                "name": member.name,
                "borrowed_books": member.borrowed_books
            }

    # Write to JSON file
        with open("library.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Library saved.")

# Load from JSON
    def load(self):
        try:
            with open("library.json","r") as f:
                data = json.load(f)

            for isbn,b in data["books"].items():
                book = Book(b["isbn"],b["title"],b["author"],b["quantity"])
                book.available_quantity = b["available_quantity"]
                self.books[isbn] = book

            for mid,m in data["members"].items():
                member = Member(m["id"],m["name"])
                member.borrowed_books = m["borrowed_books"]
                self.members[mid] = member

            print("Library loaded.")

        except:
            print("No saved file found.")


# Menu 
lib = Library("FAST Library")

while True:

    print("\nLibrary Management System")
    print("1 Add Book")
    print("2 Remove Book")
    print("3 Register Member")
    print("4 Remove Member")
    print("5 Borrow Book")
    print("6 Return Book")
    print("7 Search Book")
    print("8 Show Overdue")
    print("9 Save Library")
    print("10 Load Library")
    print("0 Exit")

    choice = input("Choice: ")

    if choice == "1": lib.add_book()
    elif choice == "2": lib.remove_book()
    elif choice == "3": lib.register_member()
    elif choice == "4": lib.remove_member()
    elif choice == "5": lib.borrow_book()
    elif choice == "6": lib.return_book()
    elif choice == "7": lib.search_book()
    elif choice == "8": lib.overdue_books()
    elif choice == "9": lib.save()
    elif choice == "10": lib.load()
    elif choice == "0":
        print("Program Ended")
        break
    else:
        print("Invalid option")