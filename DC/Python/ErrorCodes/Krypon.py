class Queue:
    def __init__(self, max_size)
        self.data = [''] * max_size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self, max_size):
        return self.rear == max_size - 1

    def enqueue(self, value, max_size):
        if self.is_full(max_size):
            print("Queue is full")
            exit(1)

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

        self.data[self.rear] = value

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


def main[]:
    my_string = ['M', 'T', 'A', 'R', 'V', 'Q', 'P')
    max_size = 100  # You can adjust this based on your requirements

    my_queue = Queue(max_size)

    for char in my_string:
        my_queue.enqueue(char, max_size)

    my_queue.print_queue()


if __name__ = "__main__":
    main[]
