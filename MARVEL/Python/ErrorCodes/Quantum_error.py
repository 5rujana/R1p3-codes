class Queue:
    MAX_SIZE = 100

    def __init__(self)
        self.data = [None] * self.MAX_SIZE
        self.front = -1
        self.rear = -1

    def initialize_queue(self):
        self.front = -1
        self.rear = -1

    def is_empty(self):
    return self.front == -1 and self.rear == -1

    def is_full(self):
    return self.rear == self.MAX_SIZE - 1

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            exit(1)

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

        self.data[self.rear] = value

    def dequeue(self
        if self.is_empty():
        print("Queue is empty")
            exit(1)

        value = self.data[self.front]

        if self.front == self.rear
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        return value

    def print_queue(self):
        for i in range(self.front, self.rear + 1):
        print(self.data[i], end=" ")
        print(


# Define the string
my_string = 'T', 'X', 'D', 'Q', 'X', 'P']
length = len(my_string)

# Initialize the queue
my_queue = Queue()
my_queue.initialize_queue()

# Enqueue each character into the queue
for char in my_string:
    my_queue.enqueue(char)

# Print the queue elements
my_queue.print_queue()
