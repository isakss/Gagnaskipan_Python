class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

def size(root):
    if root == None:
        return 0
    
    return 1 + size(root.left) + size(root.right)

def height(root):
    if root == None:
        return -1

    return 1 + max(height(root.left), height(root.right))

def nodes_on_level(root, level):
    if root == None:
        return 0
    if level == 0:
        return 1
    
    return nodes_on_level(root.left, level - 1) + nodes_on_level(root.right, level - 1)

def sum_tree(root):
    if root == None:
        return 0
    
    return root.data + (sum_tree(root.left) + sum_tree(root.right))

def is_sumtree1(root):
    if root == None or root.left == root.right == None:
        return True
    
    return root.data == (sum_tree(root.left) + sum_tree(root.right)) and is_sumtree1(root.left) and is_sumtree1(root.right)

def is_sumtree2(root):
    if root == None:
        return (True, 0)
    
    if root.right == root.left == None:
        return(True, root.data)
    
    left = is_sumtree2(root.left)
    right = is_sumtree2(root.right)

    return ((root.data == left[1] + right[1]) and (left[0] and right[0]), root.data + left[1] + right[0])

def find_path(p, q):
    if p == None:
        return []
    
    if p is q:
        return [q]
    
    left = find_path(p.left, q)
    right = find_path(p.right, q)

    if left != []:
        return [p] + left
    elif right != []:
        return [p] + right
    
    return []

def bst_min(root):
    if root == None:
        return None
    
    if root.left == root.right == None:
        return root.data
    
    return bst_min(root.left)

def bst_max(root):
    if root == None:
        return None
    
    if root.left == root.right == None:
        return root.data
    
    return bst_max(root.right)

if __name__ == "__main__":
    root = BinaryTreeNode(9, BinaryTreeNode(8), BinaryTreeNode(10))

    print(size(root))
    print(height(root))
    print(nodes_on_level(root, 1))

    root2 = BinaryTreeNode(20, BinaryTreeNode(10), BinaryTreeNode(10))

    print(is_sumtree1(root2))
    print(is_sumtree2(root2))

    p, q = BinaryTreeNode(6), BinaryTreeNode(7)

    root3 = BinaryTreeNode(10, BinaryTreeNode(11, BinaryTreeNode(13), p), BinaryTreeNode(12, q))

    print(find_path(p, q))
    print("->".join([str(x) for x in find_path(root3, q)]))

    root4 = BinaryTreeNode(9, BinaryTreeNode(3, BinaryTreeNode(2), BinaryTreeNode(8)), BinaryTreeNode(19, BinaryTreeNode(14, BinaryTreeNode(), BinaryTreeNode(15)), BinaryTreeNode(28)))

    print(bst_min(root4))
    print(bst_max(root4))
    
