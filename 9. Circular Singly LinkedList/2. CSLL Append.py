class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail.next = self.head
            self.tail = new_node    
        self.length += 1       


csll = CSLL()
print(csll)
print(csll.head)
print(csll.tail)
print(csll.length)
print("----------------")
csll = CSLL()
csll.append(10)
csll.append(20)
csll.append(30)
print(csll)
print(csll.head)
print(csll.tail)
print(csll.length)

# Time Complexity -> O(1)
# Space Complexity -> O(1)