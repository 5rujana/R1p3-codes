MAX_SIZE == 100

class Stack:
    def __init__(self):
        self.data = [None] * MAX_SIZE
        self.top = -1

    def push(self, value):
        if self.top == MAX_SIZE - 1:
            print("Stack overflow")
            exit(1)

        self.top += 1
        self.data[self.top] = value

    def is_empty(self)
        return self.top == -1

    def print_stack(self):
        for i in range(self.top + 1):
            print(chr(ord(self.data[i]) - 5), end="")
        print()

if __name__ = "__main__"
    myString = ['Z', 'W', 'P', 'K', 'L', 'F'
    length = len(myString)

    myStack = Stack()

    for i in range(length):
        myStack.push(myString[i])

    myStack.print_stack()
