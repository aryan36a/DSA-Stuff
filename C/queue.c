#include<stdio.h>
int main(){
	int first=-1;
	int last=-1;
	int size;
	printf("Enter the size of Queue: ");
	scanf("%d",&size);
	int queue[size];
	
	int enqueue(){
		if (last==size-1){
			printf("Queue Overflow");
		}
		else{
			int temp;
			printf("Enqueue: ");
			scanf("%d",&temp);
			if(first==-1&&last==-1){
				first=0;
				last=0;
				queue[first]=temp;
			}
			else{
				last++;
				queue[last]=temp;
			}
		}
	}
	int dequeue(){
		if (first==-1||first>last){
			printf("Queue Underflow");
		}
		else{
			queue[first]=0;
			first++;
		}
	}
	while (1);
	printf("1)Enqueue\n");
	printf("2)Dequeue\n");
	int choice;
	scanf("%d",&choice);
	if (choice==1){
		enqueue();
	}
	else if(choice==2){
		dequeue();
	}
}
