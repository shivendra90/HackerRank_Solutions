#!/bin/python3

import os

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode
    if head is None:
        return new_node
    else:
        #current = head
        while head.next is not None:
            head = head.next
        
        head.next = new_node
        return head


n1 = SinglyLinkedListNode(10)
n2 = SinglyLinkedListNode(24)
l1 = SinglyLinkedList()

print(insertNodeAtTail(n1, l1))
