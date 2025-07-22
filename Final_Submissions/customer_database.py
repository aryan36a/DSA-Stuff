import os
customer_list = []

def menu():
    print("1)Enter customer ID")
    print("2)Locate customer ID(Linear)")
    print("3)Locate customer ID(Binary)")
    print("4)Display Database")
    print("5)Exit")

def enter_data():
    id = int(input("Enter Customer ID: "))
    os.system('cls')
    if id not in customer_list:
        customer_list.append(id)
    else:
        print("Customer ID already in database")

def linear_search():
    target = int(input("Enter ID to search: "))
    for i in range(len(customer_list)):
        if customer_list[i] == target:
            print("Customer ID", target, "is at", i)
            return
    print("Target not found in database")

def binary_search():
    if not customer_list:
        print("Database is empty. Please add customer IDs first.")
        return
    sorted_list = sorted(customer_list)
    target = int(input("Enter ID to search: "))
    min_idx = 0
    max_idx = len(sorted_list) - 1
    while min_idx <= max_idx:
        mid = min_idx+(max_idx-min_idx)//2
        if sorted_list[mid]==target:
            print("Customer ID", target, "is at index", mid,)
            return
        elif sorted_list[mid]>target:
            max_idx=mid-1
        else:
            min_idx=mid+1
    print("Target not found in database")

while True:
    menu()
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            enter_data()
        case 2:
            linear_search()
        case 3:
            binary_search()
        case 4:
            print(customer_list)
        case 5:
            print("Exiting Program")
            os.system('cls')
            break
        case _:
            print("Not a valid input")