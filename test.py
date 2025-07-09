from collections import Counter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Library Program")

lib_data = {}
member_count = 0
book_count = 0

# --- Functions ---
def add_data():
    global member_count, book_count
    user_name = name_entry.get().strip()
    book_name = book_entry.get().strip()
    if not user_name:
        output_label.configure(text="Name cannot be empty!")
        return
    if user_name not in lib_data:
        lib_data[user_name] = []
        member_count += 1
    if book_name:
        lib_data[user_name].append(book_name)
        book_count += 1
        output_label.configure(text=f"Added '{book_name}' for {user_name}")
    else:
        output_label.configure(text="Book name cannot be empty!")

def disp_data():
    if not lib_data:
        output_label.configure(text="No data to display.")
    else:
        display = "\n".join(f"{k}: {v}" for k, v in lib_data.items())
        output_label.configure(text=display)

def avg():
    if member_count == 0:
        output_label.configure(text="No members to calculate average.")
    else:
        avg_val = book_count / member_count
        output_label.configure(text=f"Average books borrowed: {avg_val:.2f}")

def not_borrowed():
    temp = [name for name in lib_data if not lib_data[name]]
    if temp:
        output_label.configure(text="No books borrowed: " + ", ".join(temp))
    else:
        output_label.configure(text="All members have borrowed books.")

def min_borrowed():
    all_books = []
    for books in lib_data.values():
        all_books.extend(books)
    if not all_books:
        output_label.configure(text="No books have been borrowed yet!")
        return
    book_count_dict = Counter(all_books)
    min_count = min(book_count_dict.values())
    least_borrowed = [book for book, count in book_count_dict.items() if count == min_count]
    output_label.configure(text=f"Least borrowed book(s): {least_borrowed} ({min_count} times)")

def max_borrowed():
    all_books = []
    for books in lib_data.values():
        all_books.extend(books)
    if not all_books:
        output_label.configure(text="No books have been borrowed yet!")
        return
    book_count_dict = Counter(all_books)
    max_count = max(book_count_dict.values())
    most_borrowed = [book for book, count in book_count_dict.items() if count == max_count]
    output_label.configure(text=f"Most borrowed book(s): {most_borrowed} ({max_count} times)")

# --- GUI Layout ---
title_label = customtkinter.CTkLabel(app, text="Library Program", font=("Arial", 24))
title_label.pack(pady=10)

frame = customtkinter.CTkFrame(app)
frame.pack(pady=10)

name_label = customtkinter.CTkLabel(frame, text="Member Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = customtkinter.CTkEntry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

book_label = customtkinter.CTkLabel(frame, text="Book Name:")
book_label.grid(row=1, column=0, padx=5, pady=5)
book_entry = customtkinter.CTkEntry(frame)
book_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = customtkinter.CTkButton(frame, text="Add Data", command=add_data)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

button_frame = customtkinter.CTkFrame(app)
button_frame.pack(pady=10)

disp_button = customtkinter.CTkButton(button_frame, text="Display Data", command=disp_data)
disp_button.grid(row=0, column=0, padx=5)

avg_button = customtkinter.CTkButton(button_frame, text="Average Books", command=avg)
avg_button.grid(row=0, column=1, padx=5)

not_borrowed_button = customtkinter.CTkButton(button_frame, text="Not Borrowed", command=not_borrowed)
not_borrowed_button.grid(row=0, column=2, padx=5)

min_borrowed_button = customtkinter.CTkButton(button_frame, text="Least Borrowed", command=min_borrowed)
min_borrowed_button.grid(row=0, column=3, padx=5)

max_borrowed_button = customtkinter.CTkButton(button_frame, text="Most Borrowed", command=max_borrowed)
max_borrowed_button.grid(row=0, column=4, padx=5)

output_label = customtkinter.CTkLabel(app, text="", wraplength=650, justify="left")
output_label.pack(pady=20)

app.mainloop()