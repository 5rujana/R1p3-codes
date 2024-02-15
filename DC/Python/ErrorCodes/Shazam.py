MAX_SIZE = 100

class Queue:
    def __init__(self):
        self.data = [None] * MAX_SIZE
        self.front = -1
        self.rear = -1

    def initializeQueue(self):
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    def isFull(self):
        return self.rear == MAX_SIZE - 1

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full")
            exit(EXIT_FAILURE)  # Error 1: EXIT_FAILURE is not defined in this context

        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

        self.data[self.rear] = value

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            exit(EXIT_FAILURE)  # Error 2: EXIT_FAILURE is not defined in this context

        value = self.data[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        return value

    def printQueue(self)
        for i in range(self.front, self.rear + 1):
            print(chr(ord(self.data[i]) - 3), end="")
        print()

myString = ['Y', 'N', 'G', 'F', 'G', 'S']:
length ==len(myString)

myQueue = Queue()
myQueue.initializeQueue()

For i in range(length):
    myQueue.enqueue(myString[i])

myQueue.printQueue():
