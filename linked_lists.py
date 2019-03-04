#! python3
# Implementation of linked lists in Python

class Node:
    
    def __init__(self, value = None, go = None):
        self.value = value
        self.go = go
    
class LinkedList:

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

    # Display entire linked list in two ways. (We are cheating a little by storing
    # the values in a Python list but this will save many lines of code when
    # implementing the .add() methods further down below.)
    def display_fwd(self):
        node = self.head
        result = []
        while node:
            #print(node.value, end = ' ')
            result.append(node.value)
            node = node.go
        #print('')
        return result

    def display_back(self):
        node = self.head
        result = []
        while node:
            #print(node.value, end = ' ')
            result.insert(0, node.value)
            node = node.go
        #print('')
        return result

    def display(self):
        return self.display_fwd()

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

    # Two methods for adding two lists of numbers treating each list as a
    # concatenated number.
    def add_fwd(self, other):
        try:
            return int(''.join([str(i) for i in self.display_fwd()])) + \
                int(''.join([str(i) for i in other.display_fwd()]))
        except:
            raise Exception('Cannot add lists containing strings.')

    def add_back(self, other):
        try:
            return int(''.join([str(i) for i in self.display_back()])) + \
                int(''.join([str(i) for i in other.display_back()]))
        except:
            raise Exception('Cannot add lists containing strings.')