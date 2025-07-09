lib_data={}
member_count=0
book_count=0
temp=[]
books={}
def menu():
	print("=============")
	print("1)Add Data")
	print("2)Display Data")
	print("3)Display Average Books Borrowed")
	print("4)Display the students who have not borrowed any books")
	print("0)Exit Program")
	print("=============")

def add_data():
	global member_count
	global book_count
	user_name=input("Enter name: ")
	book_name=input("Enter book name: ")
	if not user_name:
		print("Name cannot be empty!1")
	else:
		if user_name not in lib_data:
			lib_data[user_name]=[]
			member_count+=1
	if book_name:
		lib_data[user_name].append(book_name)
		book_count+=1
	
def disp_data():
	print(lib_data)
	
def avg():
	global member_count
	global book_count
	print("The Average books borrowed is: ",member_count/book_count)

def not_borrowed():
	for name in lib_data:
		if not lib_data[name]:
			temp.append(name)
	print("The students who have not borrowed any books: ",temp)
def min_borrowed():
	books=Counter(lib_data.items())
	print(books)
while True:
	menu()
	choice=int(input("Enter your choice: "))
	match choice:
		case 1:
			add_data()
		case 2:
			disp_data()
		case 3:
			avg()
		case 4:
			not_borrowed()
		case 5:
			min_borrowed()
		case 0:
			print("Exiting Program....")
			break
		case _:
			print("TBI")
