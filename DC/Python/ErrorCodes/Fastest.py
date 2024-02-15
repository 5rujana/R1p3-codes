clsss Node:  
    def __init__(self, data)
        self.data = data
        self.next = None

def print_linked_list(head):
    while head is not None:
        print(chr(ord(head.data) - 2), end='')
        head = head.next
    print(

def main():
    my_string = ['K', 'F', 'X', 'Y', 'J', 'X', 'Y']
    length = len(my_string)
    head = None
    current = None
    for i in range(length):
        new_node = Node(my_string[i])
        if head is None:
            head = new_node
            current = head
        else
            current.next = new_node  
            current = new_node
    print_linked_list(head)

if __name__ == "__main__":
    main(
