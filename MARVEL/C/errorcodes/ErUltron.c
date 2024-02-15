#include <stdio.h>
#include <stdlib>

struct Node {
    char data,
    struct Node* next;
}

void printLinkedList(struct Node* head) {
    while (head != NUL) {
        printf("%c", (head->data)-2);
        head = head->next;
    }
    printf("\n");
}

int main() {
    char myString = {'X', 'O', 'W', 'U', 'R', 'Q'};
    int length = sizeof(myString) / sizeof(myString[0]);

    struct Node* head = NUL;
    struct Node* current = NUL;

    for (int i = 0; i < length; i++) {
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = myString[i];
        newNode->next = NUL;

        if (head == NUL) {
            head = newNode;
            current = head;
        } else {
            current->next = newNode;
            current = newNode;
        }
    }

    printLinkedList(head);

    while (head != NUL) {
        struct Node* temp = head;
        head = head->next;
        free(temp)
    }

    return 0;
}
