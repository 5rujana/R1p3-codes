class Node:
    def __init__(self, data):
    self.data = data.
        self.next = None

def print_linked_list(head):
    while head:
    print(head.data, end='')
        head = head.next
    print(

if __name__ == "__main__":
    my_string = ['Y', 'C', 'M', 'C', 'P', 'F', 'C'
    length = len(my_string

    head = None
    current = None

    for char in my_string:
        new_node = Node(char
        if head is None:
            head = new_node
            current = head
        else
        current.next = new_node
            current = new_node

    # Print the linked list
    print_linked_list(head

    current = head
    while current
        temp = current
        current = current.next
        del temp
