#This program implements linked list functions without an encapsulating linked list class

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

#Adding to front of list
def add_to_front(data, head):
    return Node(data, head)

#Printing all elemens of list
#   Iterative

def print_list(head):
    while head != None:
        print(head.data, end=" ")
        head = head.next
    print("")
    
#   Recursive

def print_lis_rec(head):
    if head != None:
        print(head.data, end=" ")
        print_lis_rec(head.next)
    else:
        print("")

#Removing from front of list
def remove_from_front(head):
    if head == None:
        return None
    else:
        return head.next

#Adding to back of list
def add_to_back(data, head):
    if head == None:
        return Node(data, None)
    
    head.next = add_to_back(data, head.next)
    return head

#Removing from back
def remove_from_back(head):
    if head == None or head.next == None:
        return None
    
    head.next = remove_from_back(head.next)

    return head

#Recursive operations for list
def get_list_length_iterative(head):
    size_count = 0

    while head != None:
        size_count += 1
        head = head.next
    
    return size_count

def get_lis_length_recursive(head):
    if head == None:
        return 0
    else:
        return 1 + get_lis_length_recursive(head.next)

def get_sum_of_lis(head):
    if head == None:
        return 0
    elif head.next == None:
        return head.data
    else:
        return head.data + get_sum_of_lis(head.next)

#Insert an element in its rightful place in a sorted list

def insert_ordered_iterative(head, data):
    if head == None or head.data >= data:
        return Node(data, head)
    
    curr_node = head

    while curr_node != None and curr_node.next.data < data:
        curr_node = curr_node.next
    
    curr_node.next = Node(data, curr_node.next)

    return head

def insert_ordered_recursive(head, data):
    if head == None or head.data > data:
        return Node(data, head)

    head.next = insert_ordered_recursive(head.next, data)
    return head

#Reverse a given list

def reverse_lis(head):
    if head == None or head.next == None:
        return head
    curr_node = reverse_lis(head.next)
    head.next.next = head
    head.next = None
    return curr_node

#Merge two lists

def merge_lis(head1, head2):
    if head1 == None:
        return head2
    elif head2 == None:
        return head1
    elif head1.data < head2.data:
        head1.next = merge_lis(head1.next, head2)
        return head1
    else:
        head2.next = merge_lis(head1, head2.next)
        return head2
    
#Merge sort a list

def merge_sort(head):
    if head == None or head.next == None:
        return head

    node_half = head
    node = head.next

    while node != None and node.next != None:
        node_half = node_half.next
        node = node.next.next
    
    node = node_half.next
    node_half.next = None

    return merge_lis(merge_sort(head), merge_sort(node))

#Implementation of stack and queue with Node class
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        self.top = Node(data, self.top)
        self.size += 1
    
    def pop(self):
        if self.top == None:
            return None
        
        ret_val = self.top.data
        self.top = self.top.next
        self.size -= 1

        return ret_val
    
    def get_size(self):
        return self.size
    
    def __str__(self):
        ret_str = ""

        curr_node = self.top

        while curr_node != None:
            ret_str += str(curr_node.data) + " "
            curr_node = curr_node.next
        
        return ret_str

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push_back(self, data):
        if self.head == None:
            self.head = self.tail = Node(data, None)
        else:
            self.tail.next = Node(data, None)
            self.tail = self.tail.next
        
        self.size += 1
    
    def pop_front(self):
        if self.head == None:
            return None
        else:
            ret_val = self.head.data
            self.head = self.head.next

            if self.head == None:
                self.tail = self.head

            self.size -= 1
            return ret_val
    
    def get_size(self):
        return self.size
    
    def __str__(self):
        ret_str = ""
        curr_node = self.head

        while curr_node != None:
            ret_str += str(curr_node.data) + " "
            curr_node = curr_node.next
        
        return ret_str
    
if __name__ == "__main__":
    head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))

    print_list(head)

    print_list(add_to_front(7, head))

    print_list(head)

    print_lis_rec(head)

    print_lis_rec(remove_from_front(head))

    print_lis_rec(add_to_back(6, head))

    print_lis_rec(remove_from_back(head))

    print(get_list_length_iterative(head))
    print(get_lis_length_recursive(head))

    print(get_sum_of_lis(head))

    insert_ordered_recursive(head, 8)

    print_lis_rec(head)

    print_lis_rec(reverse_lis(head))

    head2 = Node(5, Node(7, Node(23, Node(25, None))))

    merge_lis(head, head2)

    print_lis_rec(merge_sort(head))

    stack = Stack()

    for i in range(10):
        stack.push(i)
    
    print(stack)

    stack.pop()

    print(stack)

    print(stack.get_size())

    queue = Queue()

    for i in range(10):
        queue.push_back(i)
    
    print(queue)

    queue.pop_front()

    print(queue)

    print(queue.get_size())



