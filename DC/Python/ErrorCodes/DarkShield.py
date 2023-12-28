class Node:
    def __init__(self, data)
        self.data = data
        self.next = None

def print_linked_list(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

def main[]:
    my_string = ['F', 'C', 'T', 'M', 'U', 'G', 'K', 'F')
    length = len(my_string)

    head = None
    current = None

    for i in range(length):
        new_node = Node(my_string[i])

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

if __name__ = "__main__":
    main[]
