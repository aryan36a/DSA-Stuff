#include<stdio.h>

int main()
{
    int size;
    printf("Enter size of hash table: ");
    scanf("%d", &size);

    int hash_table[size];
    for(int i = 0; i < size; i++) {
        hash_table[i] = -1;
    }

    printf("Enter data in hash table of size: %d\n", size);
    for(int i = 0; i < size; i++) {
        int temp = 0;
        printf("Enter Data: ");
        scanf("%d", &temp);
        int index = temp % size;
        // Linear probing
        while(hash_table[index] != -1) {
            index = (index + 1) % size;
        }
        hash_table[index] = temp;
    }

    printf("Hash table contents:\n");
    for(int i = 0; i < size; i++) {
        printf("Index %d: %d\n", i, hash_table[i]);
    }

    int del;
    printf("Enter data you want to delete from the hash table: ");
    scanf("%d", &del);

    int found = 0;
    int index = del % size;
    
    if(hash_table[index] == del) {
        hash_table[index] = -1;
        found = 1;
        printf("Data %d deleted from index %d.\n", del, index);
        break;
        }
    if(!found) {
        printf("Data %d not found in hash table.\n", del);
    }

    printf("Hash table after deletion:\n");
    for(int i = 0; i < size; i++) {
        printf("Index %d: %d\n", i, hash_table[i]);
    }

    return 0;
}