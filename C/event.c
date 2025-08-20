// Implement a real-time event processing system using a Queue data structure. The system
// should support the following features:
// • Add an Event: When a new event occurs, it should be added to the event queue.
// • Process the Next Event: The system should process and remove the event that has
// been in the queue the longest.
// • Display Pending Events: Show all the events currently waiting to be processed.
// • Cancel an Event: An event can be canceled if it has not been processed.
#include <stdio.h>
#include <string.h>
#define max 100

typedef char string[max];

int size = 0;
int first = -1;
int last = -1;

void menu() {
    printf("+++===+++===+++\n");
    printf("1)Add an event\n");
    printf("2)Process an event\n");
    printf("3)Display pending events\n");
    printf("4)Cancel an event\n");
    printf("0)Exit\n");
    printf("+++===+++===+++\n");
}

void enqueue(string queue[]) {
    string temp;
    if (last == size - 1) {
        printf("Queue Overflow\n");
    } else {
        printf("Enter Event: ");
        scanf("%s", temp);
        if (first == -1 && last == -1) {
            first = 0;
            last = 0;
        } else {
            last++;
        }
        strcpy(queue[last], temp);
        printf("Queued: %s\n", queue[last]);
    }
}

void disp(string queue[]) {
    if (first == -1 || last == -1 || first > last) {
        printf("The Queue is Empty\n");
    } else {
        for (int i = first; i <= last; i++) {
            printf("%d: %s\n", i - first + 1, queue[i]);
        }
    }
}

void dequeue(string queue[]) {
    if (first == -1 || last == -1 || first > last) {
        printf("The Queue is Already Empty\n");
    } else {
        printf("Event Processed: %s\n", queue[first]);
        first++;
        if (first > last) {
            first = -1;
            last = -1;
        }
    }
}

void remove_event(string queue[]) {
    if (first == -1 || last == -1 || first > last) {
        printf("The Queue is Already Empty\n");
    } else {
        string rm_temp;
        disp(queue);
        printf("Enter the event to remove: ");
        scanf("%s", rm_temp);
        int found = 0;
        int idx = -1;
        for (int i = first; i <= last; i++) {
            if (strcmp(queue[i], rm_temp) == 0) {
                found = 1;
                idx = i;
                break;
            }
        }
        if (found) {
            for (int i = idx; i < last; i++) {
                strcpy(queue[i], queue[i + 1]);
            }
            last--;
            if (first > last) {
                first = -1;
                last = -1;
            }
            printf("Event has been removed from the queue\n");
        } else {
            printf("The event is not in the queue\n");
        }
    }
}

int main() {
    printf("Enter size of queue: ");
    scanf("%d", &size);
    string queue[size];

    while (1) {
        menu();
        int choice;
        printf("Enter menu choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                enqueue(queue);
                break;
            case 2:
                dequeue(queue);
                break;
            case 3:
                disp(queue);
                break;
            case 4:
                remove_event(queue);
                break;
            case 0:
                printf("Exiting...\n");
                return 0;
            default:
                printf("Invalid choice\n");
        }
    }
}