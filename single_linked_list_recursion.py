class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
def linear_search(head, value):
    if head == None:
        return False
    if value == head.data:
        return True
    else:
        return linear_search(head.next, value)

def print_list(head):
    node = head

    while node != None:
        print(node.data, end=" ")
        node = node.next
    print("")

def delete_every_other(head):
    return deo_helper(head, True)

def deo_helper(head, boolean_val):
    if head == None:
        return None
    if boolean_val == True:
        head.next = deo_helper(head.next, False)
        return head
    else:
        return deo_helper(head.next, True)

def get_size(head):
    if head == None:
        return 0
    else:
        return 1 + get_size(head.next)

def get_lis_sum(head):
    if head == None:
        return 0
    else:
        return head.data + get_lis_sum(head.next)

def add_to_ordered(head, data):
    if head == None:
        head.data = data
        return head
    if head.next.data < data:
        head = head.next
        head.next.data = data
        return head
    else:
        return add_to_ordered(head.next, data)


head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
#print(linear_search(head, 3))

print(get_size(head))
print(get_lis_sum(head))


print_list(head)
head = delete_every_other(head)
print_list(head)
head = add_to_ordered(head, 7)
print_list(head)