document = ""
undo = []
redo = []

def menu():
    print("==================")
    print("1) Add Data")
    print("2) Undo")
    print("3) Redo")
    print("4) Display Data")
    print("5) Exit")
    print("==================")

def make_changes():
    global document
    print("==================")
    text = input("Enter data: ")
    print("==================")
    undo.append(document)
    document += text
    redo.clear()

def Undo():
    global document
    if undo:
        redo.append(document)
        document = undo.pop()
    print("==================")
    print(document)
    print("==================")

def Redo():
    global document
    if redo:
        undo.append(document)
        document = redo.pop()
    print("==================")
    print(document)
    print("==================")

while True:
    menu()
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            make_changes()
        case 2:
            Undo()
        case 3:
            Redo()
        case 4:
            print(document)
        case 5:
            print("Exiting.....")
            break