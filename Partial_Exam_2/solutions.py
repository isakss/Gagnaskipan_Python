
class SLL_Node:
    # THIS IMPLEMENTATION OF SINGLY-LINKED LIST NODE
    # MUST BE USED UNCHANGED, FOR TESTING PURPOSES
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


class DLL_Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL_Ordered:
    def __init__(self):
        self.header = DLL_Node()
        self.trailer = DLL_Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header

    def find_node_to_insert_at(self, value):
        if self.header.next == self.trailer or self.header.next.data > value:
            return self.header
        
        curr_node = self.header

        while curr_node.next != self.trailer and curr_node.next.data < value:
            curr_node = curr_node.next

        return curr_node
    
    def insert_at_node(self, value, node):
        new_node = DLL_Node(value, node, node.next)
        node.next = new_node
        node.prev = new_node.prev.prev
        return new_node

    def insert_ordered(self, value):
        correct_node = self.find_node_to_insert_at(value)
        self.insert_at_node(value, correct_node)
    
    def get_range_in_SLL(self, min, max):
        # THIS OPERATION SHOULD RETURN A SINGLY-LINKED LIST
        # I.E. an instance of SLL_Node which is the first node in that list
        min_node = self.find_node_to_insert_at(min)

        head = SLL_Node()
        tmp_pos = head

        curr_node = min_node.next

        while curr_node.data <= max and curr_node.next != self.trailer:
            tmp_pos.next = SLL_Node(curr_node.data)
            tmp_pos = tmp_pos.next
            curr_node = curr_node.next

        return head.next

    def __str__(self):
        ret_str = ""
        node = self.header.next
        while node != self.trailer:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


def find_index(head, value):
    if head == None:
        return -1
    elif head.data == value:
        return 0
    else:
        return 1 + find_index(head.next, value)

    
def ordered_subset(head1, head2):
    if head1 == None or head2 == None:
        return False
    elif head1.data != head2.data:
        return ordered_subset(head1, head2.next)
    elif head1.data == head2.data and head1.next != None:
        return ordered_subset(head1.next, head2)
    else:
        return True




# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    print("\nTesting DLL_ORDERED")
    dl = DLL_Ordered()
    dl.insert_ordered(17)
    dl.insert_ordered(45)
    dl.insert_ordered(12)
    dl.insert_ordered(89)
    dl.insert_ordered(23)
    dl.insert_ordered(56)
    dl.insert_ordered(34)
    dl.insert_ordered(45)
    print("dl: " + str(dl))
    dl.insert_ordered(10)
    dl.insert_ordered(23)
    dl.insert_ordered(22)
    dl.insert_ordered(71)
    dl.insert_ordered(23)
    dl.insert_ordered(45)
    dl.insert_ordered(22)
    dl.insert_ordered(98)
    print("dl: " + str(dl))

    
    print("\nTesting RANGE")
    def test_range(dl, min, max):
        print("range(" + str(min) + ", " + str(max) + "): " + str(dl.get_range_in_SLL(min, max)))

    test_range(dl, 23, 45)
    test_range(dl, 0, 100)
    test_range(dl, 45, 45)
    test_range(dl, 17, 89)
    test_range(dl, 10, 98)
    test_range(dl, 54, 76)
    test_range(dl, 20, 60)

    print("\nTesting find_index")
    #5 6 3 4
    head = SLL_Node(5, SLL_Node(6, SLL_Node(3, SLL_Node(4, None))))
    print(find_index(head, 3))
    print(find_index(head, 7))
    #5 6 3 4 5
    head = SLL_Node(5, SLL_Node(6, SLL_Node(3, SLL_Node(4, SLL_Node(5, None)))))
    print(find_index(head, 5))
    print(find_index(head, 6))
    print(find_index(head, 4))

    print("\nTesting ordered_subset")
    head1 = SLL_Node(1, SLL_Node(5, SLL_Node(6, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(5, SLL_Node(2, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(3, SLL_Node(2, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(2, SLL_Node(3, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(2, SLL_Node(5, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(2, SLL_Node(4, SLL_Node(5, SLL_Node(6, None)))))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, SLL_Node(7, None)))))))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(2, SLL_Node(100, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(0, SLL_Node(1, SLL_Node(2, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    