class MyString:
    def __init__(self, source):
        self.data = list(source)
        self.length = len(source)

    def print_string(self):
        print(''.join(self.data), end="")

    def free_string(self):
        self.data = []
        self.length = 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(head):
    while head is not None:
        head.data.print_string()
        head = head.next

def main():
    my_string = ['M', 'D', 'U', 'Y', 'L', 'V']
    length = len(my_string)

    head = None
    current = None

    for char in my_string:
        new_node = Node(MyString(char))
        
        if head is None:
            head = new_node
            current = head
        else:
            current.next = new_node
            current = new_node

    print_linked_list(head)

    while head is not None:
        temp = head
        head = head.next
        del temp

if __name__ == "__main__":
    main()
