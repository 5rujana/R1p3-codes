class Stack:
    def __init__(self, max_size):
        self.data = []
        self.top = -1
        self.max_size = max_size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, value):
        if self.is_full():
            print("Stack overflow")
            exit(1)  # Use 1 to indicate an error

        self.top += 1
        self.data.append(value)

    def print_stack(self):
        for item in self.data[: self.top + 1]:
            print(item, end="")
        print()


def main():
    # Define the string
    my_string = ['J', 'R', 'W', 'K', 'D', 'P']
    max_size = len(my_string)  # Set the maximum size

    my_stack = Stack(max_size)

    for char in my_string:
        my_stack.push(char)

    my_stack.print_stack()


if __name__ == "__main__":
    main()
