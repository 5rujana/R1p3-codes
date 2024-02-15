class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def createNode(data):
    newNode = Node(data)
    return newNode

def printLinkedList(head):
    current = head
    while current != None:
        print(chr(ord(current.data) - 3), end="")
        current = current.next
    print()

if __name__ == "__main__":
    head = createNode('Q')
    head.next = createNode('E')
    head.next.next = createNode('V')
    head.next.next.next = createNode('Z')
    head.next.next.next.next = createNode('I')
    head.next.next.next.next.next = createNode('P')

    printLinkedList(head)

    current = head
    nextNode = None
    while current != None:
        nextNode = current.next
        del current
        current = nextNode

