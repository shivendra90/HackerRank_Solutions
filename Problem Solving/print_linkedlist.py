class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node


n1 = SinglyLinkedListNode(24)
n2 = SinglyLinkedListNode(31)

list1 = SinglyLinkedList()
list1.insert_node(n1)
list1.insert_node(n2)

def printLinkedList(head):
    current = head
    while current is not None:
        print(current)
        current = current.next

printLinkedList(list1.head)