class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None  
    
    def _populate_tree_helper(self, parent_node_name, left_right_str, level):
        if parent_node_name == "":
            data_str = input("Enter the name of the root: ")
        else:
            data_str = input("*" * level + "Enter the name of the " + left_right_str + " child of " + parent_node_name + ": ")
        if data_str == "":
            return None
        return BinaryTreeNode(data_str, self._populate_tree_helper(data_str, "left", level + 1), self._populate_tree_helper(data_str, "right", level + 1))

    def populate_tree(self):
        self.root = self._populate_tree_helper("","",0)
    
    def _print_tree_preorder_rec(self, node):
        if node == None:
            return
        
        print(str(node.data), end = " ")

        self._print_tree_preorder_rec(node.left)
        self._print_tree_preorder_rec(node.right)
    
    def _print_tree_inorder_rec(self, node):
        if node == None:
            return

        self._print_tree_inorder_rec(node.left)

        print(str(node.data), end = " ")

        self._print_tree_inorder_rec(node.right)

    def _print_tree_postorder_rec(self, node):
        if node == None:
            return

        self._print_tree_postorder_rec(node.left)
        self._print_tree_postorder_rec(node.right)

        print(str(node.data), end = " ")     

    def print_tree(self):
        #Printing contents of tree in preorder
        self._print_tree_preorder_rec(self.root)
        print("")

        #Printing contents of tree in inorder
        self._print_tree_inorder_rec(self.root)
        print("")

        #Printing contents of tree in postorder
        self._print_tree_postorder_rec(self.root)
        print("")

class GeneralTreeNode:
    def __init__(self, data = None):
        self.data = data
        self.children = []

class GeneralTree:
    def __init__(self):
        self.root = None

    def populate_tree_rec(self, level = 0):
        tree_input = input()

        if tree_input == "":
            return None

        node = GeneralTreeNode(tree_input)
        level += 1

        while True:
            print(level * "   |" + "--NODE :", end=" ")
            child_node = self.populate_tree_rec(level)
            if child_node == None:
                break
            node.children.append(child_node)
        return node

    def populate_tree(self):
        print("ROOT :", end=" ")
        self.root = self.populate_tree_rec()
    
    def _print_tree_preorder(self, node):
        if node == None:
            return
        print(str(node.data), end=" ")
        for child_node in node.children:
            self._print_tree_preorder(child_node)
    
    def print_preorder(self, node):
        self._print_tree_preorder(node)
        print("")
    
    def _print_tree_postorder(self, node):
        if node == None:
            return
        for child_node in node.child:
            self._print_tree_postorder(child_node)
        print(str(node.data), end=" ")
    
    def print_postorder(self, node):
        self._print_tree_postorder(node)
        print("")
    
    def print_tree(self):
        print("PREORDER:")
        self.print_preorder(self.root)

        print("POSTORDER:")
        self.print_postorder(self.root)

if __name__ == "__main__":
    bt = BinaryTree()

    bt.populate_tree()
    bt.print_tree()

    gt = GeneralTree()

    gt.populate_tree()
    gt.print_tree()


