#!/bin/python3

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node):
    while node:
        print(node.data)
        node = node.next

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = head
        return new_node
        
    current = head
    for _ in range(position-1):
        while current.next is not None:
            current = current.next
    
    new_node.next = current.next
    current.next = new_node
    return head

llist_count = int(input())

llist = SinglyLinkedList()

for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)
    
    data = int(input())
    position = int(input())
    
    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist.head)
