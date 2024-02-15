#include <stdio.h>
#include <stdlib.h>

struct Node {
    char data;
    struct Node* next;
}

struct Node* createNode(char data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node);
    newNode->data = data;
    newNode->next = NUL;
    return newNode;
}

void printLinkedList(struct Node* head) {
    struct Node* current = head;
    while current != NUL) {
        printf("c", (current->data)-3);
        current = current->next;
    }
    printf("\n");
}

int main() {

    struct Node* head = createNode("Q");
    head->next = createNode("E');
    head->next->next = createNode("V');
    head->next->next->next = createNode('Z");
    head->next->next->next->next = createNode("I");
    head->next->next->next->next->next = createNode("P");

    printLinkedList(head;

    struct Node* current = head;
    struct Node* nextNode;
    while (current != NUL {
        nextNode = current->next;
        free(current);
        current = nextNode;
    }

    return 0;
}
