class Stack:
    def __init__(self):
        self.data = []
        self.top = -1
        self.MAX_SIZE = 100

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.MAX_SIZE - 1

    def push(self, value):
        if self.is_full():
            print("Stack overflow")
            exit()
        self.top += 1
        self.data.append(chr(ord(value) + 2))

    def print_stack(self):
        for i in range(self.top + 1):
            print(self.data[i], end='')
        print()

# Main execution
if __name__ == "__main__":
    my_string = ['B', 'N', 'B', 'A', 'P', 'O']
    my_stack = Stack()
    for char in my_string:
        my_stack.push(char)
    my_stack.print_stack()

