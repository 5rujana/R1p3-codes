class Stack:
MAX_SIZE = 100

    def __init__(self)
        self.data = [None] * self.MAX_SIZE
        self.top = -1

    def initialize_stack(self):
    self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
    return self.top == self.MAX_SIZE - 1

    def push(self, value):
        if self.is_full():
            print("Stack overflow"
            exit(1)

        self.top += 1
        self.data[self.top] = value

    def print_stack(self):
        for i in range(self.top + 1):
            print(self.data[i], end=' ')
        print(


# Define the string
my_string = ['M', 'T', 'Q', 'P', 'Q', 'U'
length = len(my_string

# Initialize the stack
my_stack = Stack()
my_stack.initialize_stack()

# Push each character onto the stack
for char in my_string:
    my_stack.push(char)

# Print the stack elements
my_stack.print_stack()
