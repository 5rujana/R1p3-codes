#include <stdio.h>
#include <stdlib.h>

struct Node {
    char data;
    struct Node* next;
}

void printLinkedList(struct Node* head) 
    while (head != NULL) 
        printf("%c", (head->data) - 2);
        head = head->next;
    
    printf("\n");
}

int main() 

    char myString[] = {'F', 'Y', 'Q', 'F', 'S', 'Y', 'N', 'X'};
    int length = sizeof(myString) / sizeof(myString[0]);

    struct Node* head = NULL;
    struct Node* current = NULL;

    for (int i = 0; i < length; i++) 

        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));  
        if (newNode == NULL) 
            printf("Memory allocation error\n");
            exit(EXIT_FAILURE);
        

        newNode->data = myString[i];
        newNode->next = NULL;

        if (head == NULL) 
            head = newNode;
            current = head;
        
        else 
            current->next = newNode;
            current = newNode;
        
    

    printLinkedList(head);

    while (head != NULL) 
        struct Node* temp = head;
        head = head->next;
        free(temp);
    

    return 0  
}
