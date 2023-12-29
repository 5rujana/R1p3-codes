class Queue:
    def __init__(self, capacity):
        self.data = []
        self.front = -1
        self.rear = -1
        self.capacity = capacity

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            exit(1)

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

        self.data.append(value)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            exit(1)

        value = self.data[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        return value

    def print_queue(self):
        for i in range(self.front, self.rear + 1):
            print(self.data[i], end="")
        print()


def main():
    my_string = ['E', 'A', 'D', 'Q', 'T', 'I']
    capacity = 10  # Choose an appropriate capacity

    my_queue = Queue(capacity)

    for char in my_string:
        my_queue.enqueue(char)

    my_queue.print_queue()


if __name__ == "__main__":
    main()
