from random import Random

class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self._header = Node()
        self._trailer = Node()
        self._trailer.prev = self._header
        self._header.next = self._trailer
        self._current_node = self._trailer
        self._size = 0

    def insert(self, data):
        new_node = Node(data, self._current_node.prev, self._current_node)
        self._current_node.prev.next = new_node
        self._current_node.prev = new_node
        self._current_node = new_node
        
        self._size += 1

    def remove(self):
        if self._size == 0:
            pass
        else:
            self._current_node.prev.next = self._current_node.next
            self._current_node.next.prev = self._current_node.prev

            if self._current_node.next == self._trailer and self._size != 1:
                self._current_node = self._current_node.prev
            else:
                self._current_node = self._current_node.next


            self._size -= 1

    def get_value(self):
        return self._current_node.data

    def move_to_next(self):
        if self._current_node.next == self._trailer:
            pass
        else:
            self._current_node = self._current_node.next

    def move_to_prev(self):
        if self._current_node.prev == self._header:
            pass
        else:
            self._current_node = self._current_node.prev

    def move_to_pos(self, pos):
        pos_counter = 0
    	
        if pos not in range(self._size):
            pass
        else:
            self._current_node = self._header.next

            while pos_counter != pos:
                self._current_node = self._current_node.next
                pos_counter += 1

    def clear(self):
        self.__init__()

    def get_first_node(self):
        return self._header.next

    def get_last_node(self):
        return self._trailer.prev

    def partition(self, low, high):
        pivot = low
        curr_pos = pivot
        low = low.prev
        self._current_node = pivot
        

        while self._current_node.next.data != self._trailer.data:
            self.move_to_next()
            curr_pos.next = self._trailer

            if pivot.data > self._current_node.data:
                low.next = self._current_node
                self._current_node.prev = low

                low = low.next
            else:
                curr_pos.next = self._current_node
                self._current_node.prev = curr_pos

                curr_pos = curr_pos.next
        
        low.next = pivot
        pivot.prev = low
        self._current_node = pivot
    
    def sort(self):
        self.quick_sort_helper(self.get_first_node(), self.get_last_node(), self._size)
        self.move_to_pos(0)

    def quick_sort_helper(self, low, high, size):        
        if size != 1:
            self.partition(low, high)
            low = self.get_first_node()
            curr_pos = self._current_node

            self.quick_sort_helper(low, curr_pos, size // 2)
            self.partition(curr_pos.next, high)

        if size == self._size:
            self.quick_sort_helper(low.next, self.get_last_node, size // 2)

    def __len__(self):
        return self._size

    def __str__(self):
        ret_str = ""

        current_node = self._header.next
        
        while current_node != self._trailer:
            ret_str += str(current_node.data) + " "
            current_node = current_node.next

        return ret_str
    
    def print_reverse_lis(self):
        curr = self._trailer.prev

        while curr != self._header:
            print(curr.data, end=" ")
            curr = curr.prev


dll = DLL()

for i in range(10):
    num = Random().randint(0,10)
    dll.insert(num)


dll.insert(5)
print(dll)
dll.sort()
print(dll)
print(dll.get_value())

for i in range(10):
    dll.remove()

dll.remove()
print(dll)