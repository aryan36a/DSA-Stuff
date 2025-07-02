details_struct = {}
total_books=0
total_students=0
#===========================
#menu
#===========================
def menu_display():
    print("===============")
    print("Menu")
    print("1)Add Data")
    print("2)Display Data")
    print("3)Find Average Books Borrowed")
    print("4)Least Borrowed")
    print("5)Most Borrowed")
    print("6)No books borrowed")
    print("7)Frequently borrowed book")
    print("8)Exit")
    print("===============")
#============================
#Adding Data
#============================
def add_data():
    name = input("Enter the name: ")
    if name not in details_struct:
        details_struct[name] = []
    book_name = input("Enter book name: ")
    details_struct[name].append(book_name)
#=============================
#Display
#=============================
def disp_data():
    for key, value in details_struct.items():
        print(f"{key}: {value}")
#=============================
#Find average books borrowed
#=============================
def avg_books():
    total_books=sum(len(books) for books in details_struct.values())
    total_students=len(details_struct.keys())
    if total_students>0:
        average=total_books/total_students
        print(f"The average books borrowed is: {average}")
    else:
        print("No students entred to calculate")
#=============================
#Least borrowed
#=============================



while True:
    menu_display()
#===========================
#selector
#===========================
    value = (input("Choose option: "))
    match value:
        case "1":
            add_data()
        case "2":
            disp_data()
        case "3":
            avg_books()
        case "8":
            print("Exiting.....")
            break