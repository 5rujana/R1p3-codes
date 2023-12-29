class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(head):
    while head is not None:
        print(head.data, end="")
        head = head.next
    print()

def main():
    my_string = ['K', 'H', 'O', 'P', 'H', 'W']
    length = len(my_string)

    head = None
    current = None

    for char in my_string:
        new_node = Node(char)
        
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
