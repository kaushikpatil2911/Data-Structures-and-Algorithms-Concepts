class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

class LinkedList1:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

new_linked_list = LinkedList(10)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)
print(new_linked_list.length)

new_linked_list1 = LinkedList1()
print(new_linked_list1.length)

# Time Complexity -> O(1)
# Space Complexity -> O(1)