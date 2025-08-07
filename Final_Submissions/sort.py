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
    print("6)Display Top 5 Salaries")
    print("0)Exit")
    print("==================")

#Add Data
def add_data():
    salaries.append(float(input("Enter Employee Salary: ")))

#Bubble Sort
def bubble_sort(salaries):
    print("3)Selection sort")
    print("4)Print Data")
    global bubble_sort_list
    bubble_sort_list=salaries.copy()
    for i in range(len(bubble_sort_list)):
        for j in range(len(bubble_sort_list)-1):
            if bubble_sort_list[j]>bubble_sort_list[j+1]:
                bubble_sort_list[j],bubble_sort_list[j+1]=bubble_sort_list[j+1],bubble_sort_list[j]
    return(bubble_sort_list)

#Selection Sort
def selection_sort(salaries):
    global selection_sort_list
    selection_sort_list=salaries.copy()
    for i in range(len(selection_sort_list)):
        min_idx=i
        for j in range(i+1,len(selection_sort_list)):
            if selection_sort_list[j]<selection_sort_list[min_idx]:
                min_idx=j
        selection_sort_list[min_idx], selection_sort_list[i]=selection_sort_list[i],selection_sort_list[min_idx]
    return selection_sort_list
#Sorting check
def sort_check():
    if not salaries:
        print("No data available")
    else:
        if bubble_sort_list==selection_sort_list:
            print("The sort is same for both the sorting methods")
        else:
            print("Error")

#Display top 5 salaries
def top_salaries():
    temp=[]
    if len(salaries)>=5:
        bubble_sort(salaries)
        for i in range(1,6):
            temp.append(bubble_sort_list[len(bubble_sort_list)-i])
        print(temp)
    else:
        print("Not Enough Data")

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
            print("Bubble Sort: ",bubble_sort(salaries))
        case 3:
            print("Selection Sort: ",selection_sort(salaries))
        case 4:
            print(salaries)
        case 5:
            sort_check()
        case 6:
            top_salaries()
        case 0:
           exit_code()
           break
        case _:
            print("Invalid Choice")