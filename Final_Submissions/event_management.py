import os
import time
events=[]

#Menu
def menu():
    print("===============")
    print("1)Add An Event")
    print("2)Process Next Event")
    print("3)Display Pending Events")
    print("4)Cancel An Event")
    print("5)Exit")
    print("===============")

#Add Event
def add_event():
    events.append(str(input("Enter Event Name: ")))

#Process next event
def process_event():
    print("The event to be processed: ",events[0])
    print("Processing",end='')
    for i in range(5):
        time.sleep(0.5)
        print(".",end='')
    events.pop(0)
    print("The event has been processed")

#Remove Event
def remove_event():
    if not events:
        print("No event pending")
    else:
        print(events)
        event=str(input("Enter the event you want to remove: "))
        if event in events:
            events.remove(event)
            print("The event ",event," has been removed")
        else:

            print("Event is not present in pending list")
#Driver Code
while True:
    menu()
    match int(input("Enter your choice: ")):
        case 1:
            add_event()
        case 2:
            if events:
                process_event()
            else:
                print("No event pending to process")
        case 3:
            print("The pending events are: ",events)
        case 4:
            remove_event()
        case 0:
            break
        case _:
            print("Invalid Input")