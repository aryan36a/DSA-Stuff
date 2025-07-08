Document=[]
undo=[]
def menu():
    print("==================")
    print("1)Add Data")
    print("2)Undo")
    print("3)Redo")
    print("4)Display Data")
    print("5)Exit")
    print("==================")

def make_changesl():
    print("==================")
    text=input("Enter data: ")
    print("==================")
    Document.append(text)

def Undo():
    undo.append(Document.pop(len(Document)-1))
    print("==================")  
    print(Document)
    print("==================")

def Redo():
    Document.append(undo.pop(len(undo)-1))
    print("==================")
    print(Document)
    print("==================")

while True:
    menu()
    choice=int(input("Enter your choice: "))
    match choice:
        case 1:
            make_changesl()
        case 2:
            Undo()
        case 3:
            Redo()
        case 4:
            print(Document)
        case 5:
            print("Exiting.....")
            break