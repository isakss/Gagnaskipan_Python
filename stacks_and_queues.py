class IndexOutOfBounds(Exception):
    pass

class Empty(Exception):
    pass

# Stack class goes here:

class Stack:
    def __init__(self, capacity=4):
        self._capacity = capacity
        self._arr = [0] * self._capacity
        self._size = 0
    
    def push(self, value):
        if self._size == self._capacity:
            self.resize()
        
        self._arr[self._size] = value
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise Empty()
        else:
            removed_elem = self._arr[self._size]
            self._arr[self._size] = None
            self._size -= 1

            return removed_elem 

    def resize(self):
        self._capacity *= 2
        new_stack = Stack(self._capacity)

        for i in range(self._size):
            new_stack._arr[i] = self._arr[i]
        
        self._arr = new_stack._arr
        
    def __str__(self):
        return_str = ""

        for i in range(self._size - 1):
            return_str += str(self._arr[i]) + ", "
        
        return_str += str(self._arr[self._size - 1])

        return return_str

# Stack tests:

print("# STACK TESTS \n")

new_stack = Stack()

for i in range(10):
    new_stack.push(i)

print(new_stack)

print(new_stack.pop())

print(new_stack)

new_stack.push(12)

print(new_stack)

# Queue class goes here:

class Queue:
    def __init__(self, capacity=4):
        self._capacity = capacity
        self._arr = [0] * self._capacity
        self._size = 0
        self._front = 0

    def add(self, value):
        if self._size == self._capacity:
            self.resize()
        
        self._arr[self._size] = value
        self._size += 1
    
    def remove(self):
        if self._size == 0:
            raise Empty()

        removed_elem = self._arr[self._front]
        self._arr[self._front] = None

        for i in range(self._size):
            self._arr[i] = self._arr[i + 1]
        
        self._size -= 1
        
        return removed_elem

    def resize(self):
        self._capacity *= 2
        new_queue = Queue(self._capacity)

        for i in range(self._size):
            new_queue._arr[i] = self._arr[i]
        
        self._arr = new_queue._arr
    
    def __str__(self):
        return_str = ""

        for i in range(self._size - 1):
            return_str += str(self._arr[i]) + ", "
        
        return_str += str(self._arr[self._size - 1])

        return return_str

# Queue tests:

print("# QUEUE TESTS \n")

new_queue = Queue()

for i in range(20):
    new_queue.add(i)

print(new_queue)

print(new_queue.remove())

print(new_queue)
    
        

    
