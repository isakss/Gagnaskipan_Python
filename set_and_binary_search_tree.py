class BST_Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def add(self, value):
       self.root = self.add_rec(value, self.root)

    def add_rec(self, value, node):
        if node == None:
            new_node = BST_Node(value)
            return new_node
        elif node.data > value:
            node.left = self.add_rec(value, node.left)
        else:
            node.right = self.add_rec(value, node.right) 
        return node
    
    def _print_tree_inorder_rec(self, node):
        if node == None:
            return "" 
        
        string = ""

        string += self._print_tree_inorder_rec(node.left)

        string += str(node.data) + " "

        string += self._print_tree_inorder_rec(node.right)

        return string

    def find_rec(self, value, node):
        if node == None:
            return False
        elif value > node.data:
            return self.find_rec(value, node.right)
        elif value < node.data:
            return self.find_rec(value, node.left)
        else:
            return True
    
    def contains(self, value):
        return self.find_rec(value, self.root)

    def get_size_rec(self, node):
        if node == None:
            return 0

        return (self.get_size_rec(node.left) + 1 + self.get_size_rec(node.right))
    
    def __len__(self):
        tree_len = 0
        tree_len = self.get_size_rec(self.root)
        return tree_len

    def __str__(self):
        ret_str = ""
        
        ret_str += self._print_tree_inorder_rec(self.root)

        return ret_str

if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.add(8)
    bst.add(12)
    bst.add(2)

    print(bst)

    print(bst.contains(8))
    print(bst.contains(2))
    print(bst.contains(34))

    print(len(bst))
