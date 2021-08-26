class Node:
    def __init__(self, data=None, prev=None, next=None):
        self._data = data
        self._prev = prev
        self._next = next

class DLL_Dequeue:
    def __init__(self):
        self._head = Node("HEAD SENTINEL")
        self._tail = Node("TAIL SENTINAL", self._head)
        self._head._next = self._tail
        self._size = 0
    
    def push_front(self, value):
        new_node = Node(value, self._head, self._head._next)
        self._head._next = new_node
        new_node._next._prev = new_node

        self._size += 1

    def push_back(self, value):
        new_node = Node(value, self._tail._prev, self._tail)
        self._tail._prev = new_node
        new_node._prev._next = new_node

        self._size += 1
    
    def remove_front(self):
        if self._head._next == self._tail:
            pass
        else:
            self._head._next = self._head._next._next
            self._head._next._prev = self._head

            self._size -= 1
    
    def remove_back(self):
        if self._tail._prev == self._head:
            pass
        else:
            self._tail._prev = self._tail._prev._prev
            self._tail._prev._next = self._tail

            self._size -= 1

    def get_first(self):
        return self._head._next._data
    
    def get_last(self):
        return self._tail._prev._data
    
    def get_size(self):
        return self._size
    
    def __str__(self):
        curr = self._head._next
        ret_str = ""

        while curr != self._tail:
            ret_str += str(curr._data) + " "
            curr = curr._next
        
        return ret_str
    
    def print_rev_lis(self):
        curr = self._tail._prev
        
        while curr != self._head:
            print(curr._data, end=" ")
            curr = curr._prev
        print()

class DLL_PosList:
    def __init__(self):
        self._head = Node()
        self._tail = Node()
        self._head._next = self._tail
        self._tail._prev = self._head
        self._current = self._tail
        self._pos = 0
        self._size = 0

    def insert(self, data):
        node = Node(data, self._current._prev, self._current)
        node._prev._next = node
        node._next._prev = node
        self._current = node
        self._size += 1
    
    def is_empty(self):
        return self._head == self._tail
    
    def get_size(self):
        return self._size
    
    def get_data(self):
        return self._current._data
    
    def move_to_next(self):
        if self._current != self._tail:
            self._current = self._current._next
            self._pos += 1
    
    def move_to_prev(self):
        if self._current != self._head:
            self._current = self._current._prev
            self._pos -= 1
    
    def remove(self):
        if not self.is_empty() and self._current != self._tail:
            self._current._prev._next = self._current._next
            self._current._next._prev = self._current._prev
            self._current = self._current._next
            self._size -= 1
    
    def __str__(self):
        ret_str = ""
        curr = self._head._next

        while curr != self._tail:
            ret_str += str(curr._data) + " "
            curr = curr._next
        
        return ret_str

    
    
if __name__ == "__main__":
    dll_dqueue = DLL_Dequeue()
    
    dll_dqueue.push_front(8)
    dll_dqueue.push_front(7)
    dll_dqueue.push_back(9)

    print(dll_dqueue)

    print(dll_dqueue.get_size())
    print(dll_dqueue.get_first())
    print(dll_dqueue.get_last())

    dll_dqueue.remove_front()

    print(dll_dqueue)

    dll_dqueue.print_rev_lis()

    dll_dqueue.remove_back()

    print(dll_dqueue)

    print("# Poslist testing: ")

    dll_poslis = DLL_PosList()

    for i in range(10):
        dll_poslis.insert(i)

    print(dll_poslis)

    print(dll_poslis.get_data())

    dll_poslis.move_to_next()

    print(dll_poslis.get_data())

    dll_poslis.remove()

    print(dll_poslis)