class sll_node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

##########################   helper functions are encouraged in these problems   ##########################

# Functions for first part
def is_asc_ordered(head, prev_value):
    if head == None:
        return True
    elif head.value >= prev_value:
        return is_asc_ordered(head.next, head.value)
    return False

def is_desc_ordered(head, prev_value):
    if head == None:
        return True
    elif head.value <= prev_value:
        return is_desc_ordered(head.next, prev_value)
    return False

def is_asc_desc_ordered(head):
    return is_asc_ordered(head, head.value) or is_desc_ordered(head, head.value)

# Functions for second part
def count_asc_helper(head, prev_value):
    if head == None:
        return 1
    elif head.value < prev_value:
        return 1 + count_asc_helper(head.next, head.value)
    return 0 + count_asc_helper(head.next, head.value)

def count_ascending_series(head):
    return count_asc_helper(head, head.value)

if __name__ == "__main__":
    print("is_asc_desc_ordered tests:")
    test_head = sll_node(1, sll_node(2, sll_node(3, None))) #1,2,3
    print(is_asc_desc_ordered(test_head))
    test_head = sll_node(3, sll_node(2, sll_node(1, None))) #3,2,1
    print(is_asc_desc_ordered(test_head))
    test_head = sll_node(1, sll_node(3, sll_node(2, None))) #1,3,2
    print(is_asc_desc_ordered(test_head))

    print("\ncount_ascending_series tests:")
    test_head = sll_node(1, sll_node(2, sll_node(3, None))) #1,2,3
    print(count_ascending_series(test_head))
    test_head = sll_node(3, sll_node(2, sll_node(1, None))) #3,2,1
    print(count_ascending_series(test_head))
    test_head = sll_node(1, sll_node(2, sll_node(3, sll_node(2, sll_node(3, sll_node(4, sll_node(2, sll_node(7, sll_node(8, None))))))))) #1,2,3,2,3,4,2,7,8
    print(count_ascending_series(test_head))
    test_head = sll_node(5, sll_node(4, sll_node(3, sll_node(2, sll_node(1, None))))) #5,4,3,2,1
    print(count_ascending_series(test_head))
    test_head = sll_node(1, sll_node(1, sll_node(1, sll_node(2, sll_node(1, None))))) #1,1,1,2,1
    print(count_ascending_series(test_head))
