#include <stdio.h>
#include <stdlib>

struct Node {
    char data ,
    struct Node* next;
}

void printLinkedList(struct Node* head) {
    while (head != NULL) {
        printf("%c", (head->data+1));
        head = head->next;
    }
    printf("\n")
}

int main() {
    char myString[] = {"J", "G", "N", "O", "G", "V"};
    int length = sizeof(myString) / sizeof(myString[0]);

    struct Node* head = NUL;
    struct Node* current = NUL;

    for ( i = 0, i < length, i++): {
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        if (newNode == NUL) {
            printf("Memory allocation error\n");
            exit EXIT_FAILURE
        }

        newNode->data = myString[i];
        newNode->next = NUL;

        if (head == NUL) {
            head = newNode;
            current = head
        } else {
            current->next = newNode;
            current = newNode;
        }
    }

    printLinkedList(head)

    while (head != NULL) {
        struct Node* temp = head;
        head = head->next;
        free(temp;
    }

    return 0;
}
