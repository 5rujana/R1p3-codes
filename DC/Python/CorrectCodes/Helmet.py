class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(head):
    while head is not None:
        print(chr(ord(head.data) + 1), end="")
        head = head.next
    print()

if __name__ == "__main__":
    my_string = ['J', 'G', 'N', 'O', 'G', 'V']
    length = len(my_string)

    head = None
    current = None

    for i in range(length):
        new_node = Node(my_string[i])

        if new_node is None:
            print("Memory allocation error")
            exit(1)

        new_node.next = None

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

