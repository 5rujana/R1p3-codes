class Stack:
    MAX_SIZE = 100

    def __init__(self):
        self.data = [None] * self.MAX_SIZE
        self.top = -1

    def initialize_stack(self):
        self.top = -1

    def push(self, value):
        if self.top == self.MAX_SIZE - 1:
            print("Stack overflow")
            exit(EXIT_FAILURE)

        self.top += 1
        self.data[self.top] = value

    def is_empty(self):
        return self.top == -1

    def print_stack(self):
        for i in range(self.top + 1):
            print(self.data[i], end=' ')
        print()


# Define the string
my_string = ['U', 'R', 'K', 'F', 'G', 'A']
length = len(my_string)

# Initialize the stack
my_stack = Stack()
my_stack.initialize_stack()

# Push each character onto the stack
for char in my_string:
    my_stack.push(char)

# Print the stack elements
my_stack.print_stack()
