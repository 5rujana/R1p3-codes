MAX_SIZE = 100

class Stack:
    def __init__(self):
        self.data = [None] * MAX_SIZE
        self.top = -1

    def initialize_stack(self):
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == MAX_SIZE - 1

    def push(self, value):
        if self.is_full():
            print("Stack overflow")
            exit(1)

        self.top += 1
        self.data[self.top] = value

    def print_stack(self):
        for i in range(self.top + 1):
            print(self.data[i], end='')
        print()

if __name__ == "__main__":
    my_string = ['D', 'P', 'D', 'C', 'R', 'Q']
    length = len(my_string)

    my_stack = Stack()
    my_stack.initialize_stack()

    for i in range(length):
        my_stack.push(my_string[i])

    my_stack.print_stack()
