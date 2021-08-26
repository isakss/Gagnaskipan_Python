class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def sum_of_evens_rec(node, index):
    if node == None:
        return 0
    elif node.data % 2 == 0 or index % 2 == 0:
        return node.data + sum_of_evens_rec(node.next, index + 1)
    else:
        return sum_of_evens_rec(node.next, index + 1)

def sum_of_even_or_even(head):
    index_count = 0
    return sum_of_evens_rec(head, index_count)

def count_smaller_than_prev_rec(prev_node, curr_node):
    if prev_node == curr_node == None:
        return 0
    elif curr_node == None:
        return 0
    elif prev_node.data > curr_node.data:
        return 1 + count_smaller_than_prev_rec(prev_node.next, curr_node.next)
    else:
        return count_smaller_than_prev_rec(prev_node.next, curr_node.next)

def count_smaller_than_prev(head):
    prev_node = head
    curr_node = head.next
    return count_smaller_than_prev_rec(prev_node, curr_node)

if __name__ == "__main__":
    print("sum of even or even test")
    head = SLL_Node(1, SLL_Node(3, SLL_Node(2, SLL_Node(4, SLL_Node(2, SLL_Node(1))))))
    print(sum_of_even_or_even(head))
    head = SLL_Node(1, SLL_Node(2, SLL_Node(1, SLL_Node(0, SLL_Node(1, SLL_Node(0))))))
    print(sum_of_even_or_even(head))
    head = SLL_Node(1, SLL_Node(6, SLL_Node(2, SLL_Node(4, SLL_Node(2, SLL_Node(13))))))
    print(sum_of_even_or_even(head))
    head = SLL_Node(1, SLL_Node(5, SLL_Node(0, SLL_Node(2, SLL_Node(13, SLL_Node(0))))))
    print(sum_of_even_or_even(head))

    print("count smaller than prev test")
    head = SLL_Node(1, SLL_Node(3, SLL_Node(2, SLL_Node(4, SLL_Node(2, SLL_Node(1))))))
    print(count_smaller_than_prev(head))
    head = SLL_Node(1, SLL_Node(2, SLL_Node(1, SLL_Node(0, SLL_Node(1, SLL_Node(0))))))
    print(count_smaller_than_prev(head))
    head = SLL_Node(1, SLL_Node(6, SLL_Node(2, SLL_Node(4, SLL_Node(2, SLL_Node(13))))))
    print(count_smaller_than_prev(head))
    head = SLL_Node(1, SLL_Node(5, SLL_Node(0, SLL_Node(2, SLL_Node(13, SLL_Node(0))))))
    print(count_smaller_than_prev(head))
