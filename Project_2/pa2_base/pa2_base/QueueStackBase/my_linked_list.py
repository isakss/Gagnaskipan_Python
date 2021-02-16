class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def push_front(self, data):
        self._size += 1

        new_node = Node(data, self._head)
        self._head = new_node

        if self._tail == None:
            self._tail = self._head
    
    def pop_front(self):
        if self._head == None:
            return None
        
        self._size -= 1
        return_val = self._head.data
        self._head = self._head.next

        if self._head == None:
            self._tail = self._head

        return return_val
    
    def push_back(self, data):
        if self._tail == None:
            self.push_front(data)
        else:
            self._size += 1

            self._tail.next = Node(data, None)
            self._tail = self._tail.next

    def pop_back(self):
        current_node = self._head
        if self._tail == None:
            return None
        elif self._size == 1:
            self._tail = None
            self._head = self._tail
        else:
            while current_node.next != None:
                former_node = current_node
                current_node = current_node.next

            former_node.next = None
        
        self._size -= 1

        return current_node.data

    def get_size(self):
        return self._size

    def __str__(self):
        return_str = ""
        current_node = self._head

        while current_node != None:
            return_str += str(current_node.data) + " "
            current_node = current_node.next
        return_str += ""

        return return_str
        

