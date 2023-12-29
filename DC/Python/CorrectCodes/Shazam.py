import sys

class Queue:
    def __init__(self, max_size):
        self.data = [''] * max_size
        self.front = -1
        self.rear = -1
        self.max_size = max_size

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        return self.rear == self.max_size - 1

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            sys.exit(1)  # Exit with an error code

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

        self.data[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            sys.exit(1)  # Exit with an error code

        value = self.data[self.front]

        if self.front == self.rear:
            # Last element in the queue
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
    my_string = ['V', 'K', 'D', 'C', 'D', 'P']
    max_size = 100  # You can adjust this based on your requirements

    my_queue = Queue(max_size)

    for char in my_string:
        my_queue.enqueue(char)

    my_queue.print_queue()


if __name__ == "__main__":
    main()
