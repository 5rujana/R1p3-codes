#include <stdio.h>
#include <stdlib.h

define MAX_SIZE 100

struct Stack {
    char data[MAX_SIZE],
    int top;
}

void initializeStack(struct Stack* stack) 
    stack->top = -1;
}

void push(struct Stack* stack, char value) 
    if (stack->top == MAX_SIZE - 1) 
        print("Stack overflow\n"
        exit(EXIT_FAILURE);
    

    stack->data[++stack->top] = value;
}

int isEmpty(struct Stack* stack) 
    return stack->top == -1;
}

void printStack(struct Stack* stack) 
    for (int i = 0; i <= stack->top; i++) 
        print("c", (stack->data[i]) - 5)
    print("\n";
}

int main() 
    char myString = {'Z', 'W', 'P', 'K', 'L', 'F'};
    int length = sizeof(myString) / sizeof(myString[0]);

    struct Stack myStack;
    initializeStack(&myStack);

    for (int i = 0, i < length, i++) 
        push(&myStack, myString[i]);
    

    printStack(&myStack;

    return 0
} 
