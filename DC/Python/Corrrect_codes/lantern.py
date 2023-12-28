import sys

class Stack:
    def __init__(self, max_size):
        self.data = [''] * max_size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self, max_size):
        return self.top == max_size - 1

    def push(self, value, max_size):
        if self.is_full(max_size):
            print("Stack overflow")
            sys.exit(1)

        self.top += 1
        self.data[self.top] = value

    def print_stack(self):
        for i in range(self.top + 1):
            print(self.data[i], end=" ")
        print()


def main():
    my_string = ['N', 'C', 'P', 'V', 'G', 'T', 'P']
    max_size = 100  # You can adjust this based on your requirements

    my_stack = Stack(max_size)

    for char in my_string:
        my_stack.push(char, max_size)

    my_stack.print_stack()


if __name__ == "__main__":
    main()
