class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name} - {self.age}"        

new_person = Person("Kaushik",27)
print(new_person)


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
new_linkedlist.append(30)
print(new_linkedlist)
print(new_linkedlist.head.value)
print(new_linkedlist.tail.value)
print(new_linkedlist.length)       