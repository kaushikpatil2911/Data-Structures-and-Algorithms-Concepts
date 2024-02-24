class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result    
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1    

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self,index,value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            print("Not possible")
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            LinkedList.prepend(self,value)
        elif index == self.length:
            LinkedList.append(self, value)       
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length +=1

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self,value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                print(f"Value {value} at Index : "+str(index))
            current = current.next   
            index += 1

    def get(self,index):
        if index == -1:
            return self.tail.value
        if index < 0 or index > self.length:
            print("Not possible")
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def setv(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return 1
        return -1

    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1


new_linkedlist = LinkedList()
new_linkedlist.append(10)
new_linkedlist.append(20)
new_linkedlist.append(30)
print(new_linkedlist)
print(new_linkedlist.head.value)
print(new_linkedlist.tail.value)
print(new_linkedlist.length)
print("----------------")
new_linkedlist.prepend(40)
print(new_linkedlist)
print(new_linkedlist.head.value)
print(new_linkedlist.tail.value)
print(new_linkedlist.length) 
print("----------------")
new_linkedlist.insert(5,50)
print(new_linkedlist)
print(new_linkedlist.head.value)
print(new_linkedlist.tail.value)
print(new_linkedlist.length)
print("----------------")
print(new_linkedlist.traverse())
print(new_linkedlist.head.value)
print(new_linkedlist.tail.value)
print(new_linkedlist.length)
print("----------------")
print(new_linkedlist.search(10))
print(new_linkedlist.head.value)
print(new_linkedlist.tail.value)
print(new_linkedlist.length)
print("----------------")
print(new_linkedlist)
print(new_linkedlist.get(-1))
print(new_linkedlist.head.value)
print(new_linkedlist.tail.value)
print(new_linkedlist.length)
print("----------------")
print(new_linkedlist)
print(new_linkedlist.setv(2,100))
print(new_linkedlist)
print(new_linkedlist.head.value)
print(new_linkedlist.tail.value)
print(new_linkedlist.length)
print("----------------")
print(new_linkedlist)
print(new_linkedlist.pop_first())
print(new_linkedlist)
print(new_linkedlist.head.value)
print(new_linkedlist.tail.value)
print(new_linkedlist.length)

# Time Complexity -> O(1)
# Space Complexity -> O(1)