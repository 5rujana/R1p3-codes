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
            exit(EXIT_FAILURE)

        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

        self.data[self.rear] = value

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            exit(EXIT_FAILURE)

        value = self.data[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        return value

    def printQueue(self):
        for i in range(self.front, self.rear + 1):
            print(chr(ord(self.data[i]) - 2), end="")
        print()

myString = ['V', 'Z', 'F', 'S', 'Z', 'R']
length = len(myString)

myQueue = Queue()
myQueue.initializeQueue()

for i in range(length):
    myQueue.enqueue(myString[i])

myQueue.printQueue()
