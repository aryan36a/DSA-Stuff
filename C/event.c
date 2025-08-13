// Implement a real-time event processing system using a Queue data structure. The system
// should support the following features:
// • Add an Event: When a new event occurs, it should be added to the event queue.
// • Process the Next Event: The system should process and remove the event that has
// been in the queue the longest.
// • Display Pending Events: Show all the events currently waiting to be processed.
// • Cancel an Event: An event can be canceled if it has not been processed.
#include<stdio.h>
#include<string.h>
int main(){
    #define max 100
    int size=0;
    int first=-1;
    int last=-1;
    typedef char string[max];

    //Initialise an array of user def size
    printf("Enter size of queue: ");
    scanf("%d", &size);
    string queue[size];

    //Menu
    int menu(){
        printf("+++===+++===+++\n");
        printf("1)Add an event\n");
        printf("2)Process an event\n");
        printf("3)Display pending events\n");
        printf("4)Cancel an event\n");
        printf("+++===+++===+++\n");
    }

    //Enqueue
    int enqueue(){
        string temp;
        if(last==size-1){
            printf("Queue Overflow\n");
        }
        else{
            printf("Enter Event: ");
            scanf("%s", temp);
            if(first==-1 && last==-1){
                first=0;
                last=0;
            }
            else{
                last++;
            }
            strcpy(queue[last], temp);
            printf("Queued: %s\n", queue[last]);
        }
    }

    //Display Queue
    int disp(){
        if (first == -1 || last == -1 || first > last) {
            printf("The Queue is Empty\n");
        } else {
            for (int i = first; i <= last; i++) {
                printf("%d: %s\n", i - first + 1, queue[i]);
            }
        }
    }
    
    //Dequeue
    int dequeue(){
        if(first==-1||last==-1||first>last){
            printf("The Queue is Already Empty");
        }
        else{
            string del_temp="";
            strcpy(queue[first],del_temp);
            first++;
            printf("Event Processed\n");
        }
    }

    int remove(){
        if(first==-1||last==-1||first>last){
            printf("The Queue is Already Empty");
        }
        else{
            string rm_temp;
            disp();
            printf("Enter the event to remove: ");
            scanf("%s",&rm_temp);
            int found = 0;
            string del_temp = "";
            for(int j=first; j<=last; j++){
                if(strcmp(rm_temp, queue[j])){
                    strcpy(queue[j], del_temp);
                    for(int k=j; k<last; k++){
                        strcpy(queue[k], queue[k+1]);
                    }
                    last--;
                    found = 1;
                    printf("Event removed from Queue\n");
                    break;
                }
            }
            if(found=0){
                printf("Event not in Queue\n");
            }
        }
    }
    //Driver Code
    while (1){
        menu();
        int choice;
        printf("Enter menu choice: ");
        scanf("%d", &choice);
        switch (choice){
            case 1:
                enqueue();
                break;
            case 2:
                dequeue();
                break;
            case 3:
                disp();
                break;
            case 4:
                remove();
                break;

        }
    }
}