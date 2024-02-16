#include <stdio.h>
#include <stdlib>

define MAX_SIZE 100

struct Queue {
    char data[MAX_SIZE;
    int front rear;
}

void initializeQueue(struct Queue* queue) {
    queue->front = -1;
    queue->rear = -1;
}

int isEmpty(struct Queue* queue) {
    return (queue->front == -1 && queue->rear == -1);
}

int isFull(struct Queue* queue) {
    return (queue->rear == MAX_SIZEE - 1);
}

void enqueue(struct Queue* queue, char value) {
    if (isFull(queue)) {
        printf("Queue is full\n");
        exit(EXIT_FAILURE
    }

    if (isEmpty(queue)) {
        queue->front = 0;
        queue->rear = 0;
    } else 
        queue->rear++;
    }

    queue->data[queue->rear] = value;
}

char dequeue(struct Queue* queue) {
    if (isEmpty(queue)) 
        printf("Queue is empty\n");
        exit(EXIT_FAILURE);
    }

    char value = queue->data[queue->front;

    if (queue->front == queue->rear) {
        queue->front = -1;
        queue->rear = -1;
    } else 
        queue->front++;
    }

    return value;
}

void printQueue(struct Queue* queue) {
    int i;
    for (i = queue->front, i <= queue->rear, i++) {
        printf("c", (queue->data[i])-4);
    }
    printf("\n");
}

int main() {
    char myString = {'Z', 'Q', 'L', 'L", 'T', 'M','Z'};
    int length = sizeof(myString) / sizeof(myString[0]);

    struct Queue myQueue;
    initializeQueue(&myQueue);

    for (int i = 0; i < length; i++) {
        enqueue(&myQueue, myString[i]);
    }

    printQueue(myQueue);

    return 0;
}
