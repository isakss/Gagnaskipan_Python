from enum import Enum

class TreeNode:
    def __init__(self, value = 0, children = None):
        self.value = value
        if children == None: # ATHUGA: If default value is children = [] then every instance gets reference to same list!!
            self.children_nodes = []
        else:
            self.children_nodes = children

class WhichTree(Enum):
    RANDOM_TREE = 0
    TINY_TREE = 1
    SMALL_TREE = 2
    MEDIUM_TREE = 3

class NumericTree:
    def __init__(self):
        self.root = None
    
    def build_hardcoded_tree(self, which_tree):
        if which_tree == WhichTree.TINY_TREE:
            self.root = TreeNode(7, [TreeNode(2, [TreeNode(8)]), TreeNode(3, [TreeNode(4), TreeNode(6)])])
        if which_tree == WhichTree.SMALL_TREE:
            self.root = TreeNode(4, [TreeNode(7, [TreeNode(3), TreeNode(2), TreeNode(8, [TreeNode(5)])]), TreeNode(6), TreeNode(4, [TreeNode(1), TreeNode(9)])])
        if which_tree == WhichTree.MEDIUM_TREE:
            self.root = TreeNode(4)
            self.root.children_nodes.append(TreeNode(5))
            self.root.children_nodes.append(TreeNode(2))
            self.root.children_nodes.append(TreeNode(7))
            self.root.children_nodes[0].children_nodes.append(TreeNode(6))
            self.root.children_nodes[0].children_nodes.append(TreeNode(23))
            self.root.children_nodes[1].children_nodes.append(TreeNode(1))
            self.root.children_nodes[1].children_nodes.append(TreeNode(7))
            self.root.children_nodes[1].children_nodes.append(TreeNode(23))
            self.root.children_nodes[1].children_nodes.append(TreeNode(6))
            self.root.children_nodes[1].children_nodes.append(TreeNode(11))
            self.root.children_nodes[2].children_nodes.append(TreeNode(17))
            self.root.children_nodes[2].children_nodes.append(TreeNode(12))
            self.root.children_nodes[2].children_nodes.append(TreeNode(13))
            self.root.children_nodes[1].children_nodes[1].children_nodes.append(TreeNode(34))
            self.root.children_nodes[1].children_nodes[1].children_nodes.append(TreeNode(37))
            self.root.children_nodes[1].children_nodes[1].children_nodes.append(TreeNode(26))
            self.root.children_nodes[1].children_nodes[2].children_nodes.append(TreeNode(18))
            self.root.children_nodes[1].children_nodes[3].children_nodes.append(TreeNode(3))
            self.root.children_nodes[1].children_nodes[3].children_nodes.append(TreeNode(6))
            self.root.children_nodes[1].children_nodes[1].children_nodes[1].children_nodes.append(TreeNode(7))
            self.root.children_nodes[1].children_nodes[1].children_nodes[1].children_nodes.append(TreeNode(9))
            self.root.children_nodes[1].children_nodes[1].children_nodes[1].children_nodes.append(TreeNode(13))
    
    def sum_values_preorder(self, node, sum_of_val):
        if node.children_nodes == []:
            return node.value


        for child in node.children_nodes:
            sum_of_child = 0
            sum_of_child += node.value + self.sum_values_preorder(child, sum_of_val)
        
        sum_of_val += sum_of_child
 
        return sum_of_val

    def sum_of_all_values(self):
        sum_of_val = 0
        return self.sum_values_preorder(self.root, sum_of_val)

    def series_exists(self, number_list):
        #TODO: IMPLEMENT THIS
        return False


if __name__ == "__main__":

    tree = NumericTree()

    print("\nTINY TREE")
    tree.build_hardcoded_tree(WhichTree.TINY_TREE)
    print("VALUE SUM: " + str(tree.sum_of_all_values()))

    print("\nSMALL TREE")
    tree.build_hardcoded_tree(WhichTree.SMALL_TREE)
    print("VALUE SUM: " + str(tree.sum_of_all_values()))

    print("\nMEDIUM TREE")
    tree.build_hardcoded_tree(WhichTree.MEDIUM_TREE)
    print("VALUE SUM: " + str(tree.sum_of_all_values()))

    print("\nCHECKING SERIES")

    num_lis = [4, 2, 7, 26]
    print(str(num_lis) + ": " + str(tree.series_exists(num_lis)))

    num_lis = [4, 2, 7, 26, 7]
    print(str(num_lis) + ": " + str(tree.series_exists(num_lis)))

    num_lis = [4, 2, 7]
    print(str(num_lis) + ": " + str(tree.series_exists(num_lis)))

    num_lis = [2, 7, 26]
    print(str(num_lis) + ": " + str(tree.series_exists(num_lis)))

    num_lis = [4, 7, 12]
    print(str(num_lis) + ": " + str(tree.series_exists(num_lis)))

    num_lis = [4, 5, 23]
    print(str(num_lis) + ": " + str(tree.series_exists(num_lis)))

    num_lis = [4, 2, 1]
    print(str(num_lis) + ": " + str(tree.series_exists(num_lis)))

    num_lis = [4, 7, 13]
    print(str(num_lis) + ": " + str(tree.series_exists(num_lis)))

    num_lis = [4, 2, 7, 37, 9]
    print(str(num_lis) + ": " + str(tree.series_exists(num_lis)))
