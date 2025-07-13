from collections import defaultdict

details_struct = {}  # Stores student names and their borrowed books
book_struct = {}    # Not used in this version, can be removed or utilized later
total_books = 0
total_students = 0

#============================
# Menu
#============================
def menu_display():
    print("===============")
    print("Menu")
    print("1) Add Data")
    print("2) Display Data")
    print("3) Find Average Books Borrowed")
    print("4) Least Borrowed")
    print("5) Most Borrowed")
    print("6) No books borrowed")
    print("7) Frequently borrowed book")  # Note: This function is missing, added placeholder
    print("8) Exit")
    print("===============")

#============================
# Adding Data
#============================
def add_data():
    global total_books, total_students
    name = input("Enter the name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    if name not in details_struct:
        details_struct[name] = []
        total_students += 1
    book_name = input("Enter book name: ").strip()
    if book_name:  # Only add if book name is not empty
        details_struct[name].append(book_name)
        total_books += 1
    else:
        print("No book added for this student.")  # Handle empty book input

#=============================
# Display
#=============================
def disp_data():
    if not details_struct:
        print("No data available!")
    else:
        for key, value in details_struct.items():
            print(f"{key}: {value}")

#=============================
# Find average books borrowed
#=============================
def avg_books():
    if total_students > 0:
        average = total_books / total_students
        print(f"The average books borrowed is: {average}")
    else:
        print("No students entered to calculate")

#=============================
# Least Borrowed
#=============================
def least_borrowed():
    if not details_struct:
        print("No data available!")
        return
    book_list = []
    for books in details_struct.values():
        book_list.extend(books)
    if not book_list:
        print("No books borrowed!")
        return
    book_freq = {}
    for book in book_list:
        book_freq[book] = book_freq.get(book, 0) + 1
    min_freq = min(book_freq.values())
    least_borrowed_books = [book for book, freq in book_freq.items() if freq == min_freq]
    print("Least borrowed book(s):", least_borrowed_books)

#=============================
# Most Borrowed
#=============================
def most_borrowed():
    if not details_struct:
        print("No data available!")
        return
    book_list = []
    for books in details_struct.values():
        book_list.extend(books)
    if not book_list:
        print("No books borrowed!")
        return
    book_freq = {}
    for book in book_list:
        book_freq[book] = book_freq.get(book, 0) + 1
    max_freq = max(book_freq.values())
    most_borrowed_books = [book for book, freq in book_freq.items() if freq == max_freq]
    print("Most borrowed book(s):", most_borrowed_books)

#=============================
# No books borrowed
#=============================
def no_books():
    if not details_struct:
        print("No data available!")
        return
    no_books_list = []
    for name in details_struct:
        if not details_struct[name]:
            no_books_list.append(name)
    if not no_books_list:
        print("All students have borrowed at least one book!")
    else:
        print("Students who borrowed no books:", no_books_list)

while True:
    menu_display()
    #===========================
    # Selector
    #===========================
    value = input("Choose option: ").strip()  # Removed unnecessary parentheses
    match value:
        case "1":
            add_data()
        case "2":
            disp_data()
        case "3":
            avg_books()
        case "4":
            least_borrowed()
        case "5":
            most_borrowed()
        case "6":
            no_books()
        case "8":
            print("Exiting.....")
            break
        case _:
            print("Invalid option! Please choose 1-8.")
#Code by Aryan Sangave