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
        self._current = self._tail
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
            print(curr._data)
            curr = curr._prev


"""
class DLL:
    def __init__(self):
        self._head = Node()
        self._tail = Node()
        self._head._next = self._tail
        self._tail._prev = self._head
        self._current = self._tail
"""
    
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