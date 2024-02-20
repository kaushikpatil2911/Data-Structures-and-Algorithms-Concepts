class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = new_Node
        self.length += 1

new_linkedlist = LinkedList()
new_linkedlist.append(10)
new_linkedlist.append(20)
print(new_linkedlist.head.value)
print(new_linkedlist.tail.value)
print(new_linkedlist.length)  

# Time Complexity -> O(1)
# Space Complexity -> O(N)