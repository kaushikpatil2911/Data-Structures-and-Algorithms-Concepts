class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLL:
    def __init__(self,value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1

# class CSLL2:
#     def __init__(self,value):
#         self.head = None
#         self.tail = None
#         self.length = 0


csll = CSLL(10)
print(csll)
print(csll.head)
print(csll.tail)
print(csll.length)

# Time Complexity -> O(1)
# Space Complexity -> O(1)