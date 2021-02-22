class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

#Nodes and list WITH encapsulating class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, value):
        self.size += 1

        new_node = Node(value, self.head)
        self.head = new_node

        if self.tail == None:
            self.tail = self.head

    def push_back(self, value):
        self.size += 1

        if self.tail == None:
            self.push_front(value)
        else:
            self.tail.next = Node(value, None)
            self.tail = self.tail.next
    
    def pop_front(self):
        if self.head == None:
            return None

        self.size -= 1
        ret_val = self.head.data
        self.head = self.head.next
        
        if self.head == None:
            self.tail = self.head

        return ret_val
    
    def pop_back(self):
        current_node = self.head
        if self.tail == None:
            return None
        elif self.size == 1:
            self.tail = None
            self.head = self.tail
        else:
            while current_node.next != None:
                former_node = current_node
                current_node = current_node.next
            
            former_node.next = None

        self.size -= 1

        return current_node.data
    
    def get_size(self):
        return self.size
    
    def __str__(self):
        curr_node = self.head
        ret_str = ""

        while curr_node != None:
            ret_str += str(curr_node.data) + " "
            curr_node = curr_node.next
        
        return ret_str
            
class Stack:
    def __init__(self):
        self.container = LinkedList()

    def push(self, value):
        self.container.push_back(value)

    def pop(self):
        self.container.pop_back()

class Queue:
    def __init__(self):
        self.container = LinkedList()

    def add(self, value):
        self.container.push_back(value)

    def remove(self):
        self.container.pop_front()

lis = LinkedList()

lis.push_front(3)
lis.push_front(2)
lis.push_front(1)

print(lis)

lis.push_back(4)
lis.push_back(5)

print(lis)

lis.pop_front()
lis.pop_front()
lis.pop_front()

print(lis)

print(lis.pop_back())

print(lis)

"""
def print_list(head_element):
    while head_element != None:
        print(head_element.data, end=" ")
        head_element = head_element.next
    print("")

def push_front(head_element, value):
    #new_head = Node(value, head_element)
    #head_element = new_head

    new_head = Node()
    new_head.data = value
    new_head.next = head_element

    return new_head

def remove_front(head_element):
    if head_element == None:
        print("Cant remove from empty list!")
        pass
    else:
        new_head = head_element.next
        head_element = None

    return new_head

def push_back(head_element, value):
    if head_element == None:
        head_element = value
    else:    
        while head_element.next != None:
            head_element = head_element.next
    
        head_element.next = value


head = None
print_list(head)

head = push_front(head, 0)
head = push_front(head, 1)
head = push_front(head, 2)
head = push_front(head, 3)

print_list(head)

head = remove_front(head)

print_list(head)

push_back(head, 6)

print_list(head)
"""



