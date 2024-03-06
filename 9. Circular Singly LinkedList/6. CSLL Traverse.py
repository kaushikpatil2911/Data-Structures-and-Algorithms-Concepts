class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLL():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result       

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node    
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head   
        self.length += 1 

    def insert(self,index,value):
        new_node = Node(value)
        if index == 0:
            csll.prepend(value)
        elif index == self.length:
            csll.append(value)
        elif index > self.length or index < 0:
            print("Index out of range !!!")
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next
            if curr == self.head:
                break                


csll = CSLL()
print(csll)
print(csll.head)
print(csll.tail)
print(csll.length)
print("----------------")
csll.append(10)
csll.append(20)
csll.append(30)
print(csll)
print(csll.head.value)
print(csll.tail.value)
print(csll.length)
print("----------------")
csll.prepend(100)
csll.prepend(200)
csll.prepend(300)
print(csll)
print(csll.head.value)
print(csll.tail.value)
print(csll.length)
print("----------------")
csll.insert(13,0)
print(csll)
print(csll.head.value)
print(csll.tail.value)
print(csll.length)
print("----------------")
csll.traverse()
print(csll)
print(csll.head.value)
print(csll.tail.value)
print(csll.length)
print("----------------")

# Time Complexity -> O(n)
# Space Complexity -> O(1)