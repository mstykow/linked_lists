#! python3
# Implementation of linked lists in Python

class Node:
    
    def __init__(self, value = None, go = None):
        self.value = value
        self.go = go
    
class LinkedList:

    # head is a node which initially is None unless otherwise specified
    def __init__(self, head = None):
        self.head = head

    # Insert new nodes at the beginning of the linked list (like a stack)
    def insert(self, value):
        node = Node(value, self.head)
        self.head = node

    def size(self):
        counter = 0
        node = self.head
        while node:
            node = node.go
            counter += 1
        return counter

    def search(self, value):
        counter = 0
        node = self.head
        while node and node.value != value:
            node = node.go
            counter += 1
        if node == None:
            raise ValueError('Value not in list.')
        else:
            return 'Value located at index {}.'.format(counter)

    def reverse(self):
        temp = LinkedList()
        node = self.head
        while node:
            temp.insert(node.value)
            node = node.go
        self.head = temp.head

    # Display entire linked list.
    def display(self):
        node = self.head
        if node:
            result = str(node.value)
            node = node.go
            while node:
                result = result + ' -> ' + str(node.value)
                node = node.go
            return result
        else:
            return None

    # String-concatenate list forwards and backwards.
    def concat_fwd(self):
        node = self.head
        if node:
            result = str(node.value)
            node = node.go
            while node:
                result = result + str(node.value)
                node = node.go
            return result
        else:
            return None

    def concat_bwd(self):
        node = self.head
        if node:
            result = str(node.value)
            node = node.go
            while node:
                result = str(node.value) + result
                node = node.go
            return result
        else:
            return None

    # .delete() removes the first occurrence of a provided value. It is accomplished
    # by linking the node before the to-be-deleted node to the node after it and
    # implemented in a similar way to .search(). This time we need to keep track of the
    # preceeding node at each iteration. There is also a special case where the
    # to-be-deleted node is the list's head.
    def delete(self, value):
        if self.head.value == value:
            self.head = self.head.go
        else:
            node = self.head
            while node and node.value != value:
                temp_node = node
                node = node.go
            if node == None:
                raise ValueError('Value not in list.')
            else:
                temp_node.go = node.go

    # Two methods for adding two linked lists of numbers treating each list as a
    # concatenated number.
    def add_fwd(self, other):
        try:
            return int(''.join([i for i in self.concat_fwd()])) + \
                int(''.join([i for i in other.concat_fwd()]))
        except:
            raise Exception('Cannot add lists containing strings.')

    def add_bwd(self, other):
        try:
            return int(''.join([i for i in self.concat_bwd()])) + \
                int(''.join([i for i in other.concat_bwd()]))
        except:
            raise Exception('Cannot add lists containing strings.')