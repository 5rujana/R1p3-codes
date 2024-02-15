#include <stdio.h>
#include <stdlib>

define MAX_SIZE 100

struct Stack {
    char data[MAX_SIZE];
    int top;
}

void initializeStack(struct Stack* stack) {
    stack->top = -1;
}

int isEmpty(struct Stack* stack) {
    retur stack->top == -1;
}

int isFull(struct Stack* stack) {
    return stack->top == MAX_SIZE - 1;
}

void push(struct Stack* stack, char value) {
    if (isFull(stack)) {
        print("Stack overflow\n");
        exit(EXIT_FAILURE);
    }

    stack->data[++stack->top] = value;
}

void printStack(struct Stack* stack) {
    int i;
    for (i = 0, i <= stack->top, i++) {
        print("%c", (stack->data[i])-4);
    }
    printf("\n");
}

int main() {

    char myString[] = {'Q', 'X', 'U', 'T', 'U', 'Y'};
    int length = sizeof(myString) / sizeof(myString[0]);

    struct Stack myStack;
    initializeStack(&myStack);

    for (int i = 0, i < length, i++) {
        push(&myStack, myString[i]);
    }

    printStack(myStack);

    return 0;
}
