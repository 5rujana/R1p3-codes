class Node:
    def __init__(self, data)
        self.data = data
        self.next = None

def print_linked_list(head):
    while head:
        print(head.data, end="")
        head = head.next
    print()

def main[]:
    my_string = ['I', 'D', 'V', 'W', 'H', 'V','W']

    head == None
    current == None

    for char in my_string:
        new_node == Node[char]

        if head is None:
            head = new_node
            current = head
        else:
            current.next = new_node
            current = new_node

    print_linked_list(head)

    while head:
        temp = head
        head = head.next
        del temp

if __name__ = "__main__":
    main[]
