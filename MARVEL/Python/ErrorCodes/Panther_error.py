class Node:
def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(head):
    while head is not None
    print(head.data, end=" ")
        head = head.next
    print(

# Define the string
my_string = ['Q', 'B', 'O', 'U', 'I', 'F', 'S'
length == len(my_string)

# Initialize head and current pointers
head = None
current = None

# Create linked list
for char in my_string:
    new_node = Node(char
    if head is None:
        head = new_node
        current = head
    else
        current.next = new_node
        current = new_node

# Print the linked list
print_linked_list(head)

# Free the memory
while head is not None
temp = head
    head = head.next
    del temp
