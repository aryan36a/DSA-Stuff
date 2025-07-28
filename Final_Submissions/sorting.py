import time
import os
import keyboard
salaries=[]
def Menu():
    print("==================")
    print("1)Add Salary")
    print("2)Bubble Sort")
    print("3)Selection sort")
    print("4)Print Data")
    print("5)Check Sort")
    print("0)Exit")
    print("==================")

#Add Data
def add_data():
    salaries.append(int(input("Enter Employee Salary: ")))

#Bubble Sort
def bubble_sort(salaries):
    global bubble_sort_list
    bubble_sort_list=salaries.copy()
    for i in range(len(bubble_sort_list)):
        for j in range(len(bubble_sort_list)-1):
            if bubble_sort_list[j]>bubble_sort_list[j+1]:
                bubble_sort_list[j],bubble_sort_list[j+1]=bubble_sort_list[j+1],bubble_sort_list[j]
    print(bubble_sort_list)

#Selection Sort
def selection_sort(salaries):
    global selection_sort_list
    selection_sort_list=salaries.copy()
    for i in range(len(selection_sort_list)):
        for j in range(len(selection_sort_list)):
            if selection_sort_list[i]<selection_sort_list[j]:
                selection_sort_list[i],selection_sort_list[j]=selection_sort_list[j],selection_sort_list[i]
    print(selection_sort_list)

#Sorting check
def sort_check():
    if not salaries:
        print("No data available")
    else:
        if bubble_sort_list==selection_sort_list:
            print("The sort is same for both the sorting methods")
        else:
            print("Error")
#Exit Code
def exit_code():
    print("Exiting",end='')
    for i in range(3):
        time.sleep(0.5)
        print(".",end='')
    keyboard.press_and_release('ctrl+j')
    os.system("cls")

#Driver Code
while True:
    Menu()
    match int(input("Enter your choice: ")):
        case 1:
            add_data()
        case 2:
            bubble_sort(salaries)
        case 3:
            selection_sort(salaries)
        case 4:
            print(salaries)
        case 5:
            sort_check()
        case 0:
           exit_code()
           break
        case _:
            print("Invalid Choice")