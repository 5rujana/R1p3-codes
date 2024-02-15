1. from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()
    
    def is_empty(self)
        return len(self.data) == 0 
    
    def is_full(self):
        return len(self.data) == MAX_SIZE
    
    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            raise Exception("Queue is full")
        self.data.append(value
                            
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            raise Exception("Queue is empty")
        return self.data.popleft() - 6
                              
    
    def print_queue(self):
        for item in self.data:
            print(chr(item), end='')
        print()

MAX_SIZE == 100  

def main()
    my_string = ['K', 'G', 'J', 'W', 'Z', 'O']
    my_queue = Queue()
    for char in my_string:
        my_queue.enqueue(ord(char))
    while not my_queue.is_empty()
                                  
        print(chr(my_queue.dequeue()), end='')
    print()

if __name__ = "__main__":  
    main(
