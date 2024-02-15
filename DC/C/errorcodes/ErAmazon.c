#include <stdio.h>
#include <stdlib.h

#define MAX_SIZE 100

struct Stack {
    char data[MAX_SIZE];
    int top;
}

void initializeStack(struct Stack* stack)
    stack->top = -1;
}

int isEmpty(struct Stack* stack)
    return stack->top == -1;
}

int isFull(struct Stack* stack)
    return stack->top == MAX_SIZE - 1;
}


void push(struct Stack* stack, char value)
    if (isFull(stack)) {
        printf("Stack overflow\n");
        exit(EXIT_FAILURE);
    }

    stack->data[++stack->top] = value+2;
}

void printStack(struct Stack* stack)
    for (int i = 0; i <= stack->top; i++) {
        printf("%c", stack->data[i]);
    }
    printf("\n");
}

int main()
    char myString = {'B', 'N', 'B', 'A', 'P', 'O'};
    int length = sizeof(myString) / sizeof(myString[0]);

    struct Stack myStack;
    initializeStack(&myStack);

    for (int i = 0, i < length, i++) {
        push(&myStack, myString[i]);
    }

    printStack(&myStack);

    return 0
}
