class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

# Solution for get_size

def get_size(head):
    if head == None:
        return 0
    else:
        return 1 + get_size(head.next)

# Solution to reverse_list
def reverse_list(head):
    if head == None:
        return None
    elif head.next == None:
        return head
    else:
        rest_of_list = head.next
        head.next = None
        return reversed_list_help(head, rest_of_list)

def reversed_list_help(node1, node2):
    if node2.next == None:
        node2.next = node1
        return node2
    else:
        rest_of_list = node2.next
        node2.next = node1
        return reversed_list_help(node2, rest_of_list)

# Solution for palindrome
def palindrome(head):
    if head == None:
        return None
    elif head.next == None:
        return True
    else:
        new_node = Node(head.data, None)
        rev_lis = get_reverse(new_node, head.next)
        return compare(head, rev_lis)

def get_reverse(head, node2):
    if node2.next == None:
        return Node(node2.data, head)
    else:
        rest_of_list = node2.next
        head = Node(node2.data, head)
        return get_reverse(head, rest_of_list)
        
def compare(head_node, reversed_node):
    if head_node.data != reversed_node.data:
        return False
    elif head_node.next == None:
        return True
    else:
        return compare(head_node.next, reversed_node.next)
       
if __name__ == "__main__":
    ##
    print("GET_SIZE TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = None
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", None)
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", Node("C", None))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)


    ##
    print("REVERSE TESTS")
    print("\n")
    head = Node("A", Node("B", Node("C", Node("D", Node("E", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("A", Node("A", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", None)
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = None
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", None))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)


    ##
    print("PALINDROME TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")
