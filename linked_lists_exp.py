#! python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def int_to_list(number):
    string = str(number)
    linked_list = ListNode(int(string[0]))
    for i in range(1, len(string)):
        temp = ListNode(int(string[i]))
        temp.next = linked_list
        linked_list = temp
    return linked_list