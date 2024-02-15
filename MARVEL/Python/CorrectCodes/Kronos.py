MAX_SIZE = 100

class Stack:
    def __init__(self):
        self.data = [None] * MAX_SIZE
        self.top = -1

    def initializeStack(self):
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == MAX_SIZE - 1

    def push(self, value):
        if self.isFull():
            print("Stack overflow")
            exit(1)

        self.top += 1
        self.data[self.top] = value

    def printStack(self):
        for i in range(self.top + 1):
            print(chr(ord(self.data[i]) - 4), end="")
        print()

if __name__ == "__main__":
    myString = ['Q', 'X', 'U', 'T', 'U', 'Y']
    length = len(myString)

    myStack = Stack()
    myStack.initializeStack()

    for i in range(length):
        myStack.push(myString[i])

    myStack.printStack()
