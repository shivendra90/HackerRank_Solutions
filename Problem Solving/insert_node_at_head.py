import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node, sep):
    """Prints the elements of a singly linked list."""
    while node:
        print(node.data, end='')
        node = node.next
        if node:
            print(sep, end='')
    print()  # Newline at the end

def insertNodeAtHead(llist, data):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    if llist is None:
        return new_node
    else:
        current = new_node
        while current.next is not None:
            current = current.next
    
        current.next = llist
        llist = current
    
    return llist


if __name__ == "__main__":
    llist = None
    llist = insertNodeAtHead(llist, 1)
    llist = insertNodeAtHead(llist, 2)
    llist = insertNodeAtHead(llist, 3)
    print_singly_linked_list(llist, " ")
    