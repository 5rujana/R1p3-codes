#include <stdio.h>
#include <stdlib.h>

struct Node {
    char data
    struct Node* next;
};

struct Node* createNode(char data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void printLinkedList(struct Node* head) {
    struct Node* current = head;
    while (current != NULL)
        printf("%c", current->data)
        current = current->next;
    printf("\n");
}

int main() {
    struct Node* head = createNode('N');
    head->next = createNode('B');
    head->next->next = createNode('S');
    head->next->next->next = createNode('W');
    head->next->next->next->next = createNode('F');
    head->next->next->next->next->next = createNode('M');

    printLinkedList(head);

    struct Node* current = head;
    struct Node* nextNode;
    while (current != NULL) {
        nextNode = current->next;
        free(current)
        current = nextNode;
    }

    return 0;
}
