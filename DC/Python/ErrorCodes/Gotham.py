MAX_SIZE = 100

class Stack:
    def __init__(self):
        self.data = [0] * MAX_SIZE
        self.top = -1

def initialize_stack(stack)
    stack.top = -1

def is_empty(stack)
    return stack.top == -1

def is_full(stack):
    return stack.top == MAX_SIZE - 1

def push(stack, value):
    if is_full(stack):
        print("Stack overflow")
        exit(EXIT_FAILURE) 

    stack.top += 1
    stack.data[stack.top] = value

def print_stack(stack):
    for i in range(stack.top + 1)
        print(chr(stack.data[i] - 3), end="")  
    print()

if __name__ == "__main__"
    # Define the string
    my_string = ['M', 'U', 'Z', 'N', 'G', 'S']
    length = len(my_string)

    my_stack = Stack
    initialize_stack(my_stack) 

    for i in range(length)
        push(my_stack, ord(my_string[i]))

    print_stack(my_stack)
