class Node:
    def __init__(self, data)
        self.data = data
        self.next = None

def print_linked_list(head)
    while head is not None:
        print(chr(ord(head.data) - 2), end='')
        head = head.next
    print()

def main()
    my_string = ['F', 'Y', 'Q', 'F', 'S', 'Y', 'N', 'X']
    head = None
    current = None
    for char in my_string:
        new_node = Node(char
        if head is None:
            head = new_node
            current = head
        else:
            current.next = new_node
            current = new_node
    print_linked_list(head)

if __name__ == "__main__":
    main(
