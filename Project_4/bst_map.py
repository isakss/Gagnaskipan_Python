class NotFoundException(Exception):
    pass

class ItemExistsException(Exception):
    pass

class BST_Node:
    def __init__(self, key = None, data = None, left = None, right = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BST_Map:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root == None:
            self.root = BST_Node(key, data)
            return

        new_node = self._find_node_rec(key, self.root)

        if new_node.key == key:
            raise ItemExistsException()
        else:
            if new_node.key < key:
                new_node.right = BST_Node(key, data)
            else:
                new_node.left = BST_Node(key, data)
    
    def update(self, key, data):
        found_node = self._find_node_rec(key, self.root)

        if found_node.key == key:
            found_node.data = data
        else:
            raise NotFoundException()
    
    def _find_node_rec(self, key, node):
        if key > node.key and node.right != None:
            return self._find_node_rec(key, node.right)
        elif key < node.key and node.left != None:
            return self._find_node_rec(key, node.left)
        else:
            return node

    def find(self, key):
        found_node = self._find_node_rec(key, self.root)

        if found_node.key != key:
            raise NotFoundException()
        else:
            return found_node.data
    
    def contains(self, key):
        found_node = self._find_node_rec(key, self.root)

        if found_node.key != key:
            return False
        else:
            return True
    
    def remove(self, key):
        found_node = self._find_node_rec(key, self.root)
        
        if found_node.key != key:
            raise NotFoundException()
        elif found_node.left != None and found_node != None:
            replacement_node = self._find_right_most_of_left(found_node.left)
            parent_node = self._get_parent_node(self.root, replacement_node)
            self._remove_helper(parent_node, replacement_node)

            parent_node = self._get_parent_node(self.root, found_node)

            if parent_node != None:
                if parent_node.left == found_node:
                    parent_node.left = replacement_node
                else:
                    parent_node.right = replacement_node
            else:
                self.root = replacement_node

            replacement_node.left = found_node.left
            replacement_node.right = found_node.right
        else:
            parent_node = self._get_parent_node(self.root, found_node)
            self._remove_helper(parent_node, found_node)

    def _remove_helper(self, parent, child):
        if parent == None:
            if child.left == None and child.right == None:
                self.root = None
            else:
                if child.left == None:
                    self.root = child.right
                else:
                    self.root = child.left
            return

        if parent.left == child:
            if child.left == None:
                parent.left = child.right
            else:
                parent.left = child.left
        else:
            if child.left == None:
                parent.right = child.right
            else:
                parent.right = child.left

    def _find_right_most_of_left(self, the_node):
        if the_node.right == None:
            return the_node
        else:
            return self._find_right_most_of_left(the_node.right)
    
    def _get_parent_node(self, current_node, target_node):
        if current_node.key == target_node.key:
            return None
        
        if current_node.key > target_node.key:
            if current_node.left.key == target_node.key:
                return current_node
            else:
                return self._get_parent_node(current_node.left, target_node)
        else:
            if current_node.right.key == target_node.key:
                return current_node
            else:
                return self._get_parent_node(current_node.right, target_node)

    def _remove_none_or_one_child(self, current_node, target_node):
        if current_node.key == target_node.key:
            if target_node.left == None and target_node.right == None:
                self.root = None
            else:
                if target_node.left == None:
                    self.root = target_node.right
                else:
                    self.root = target_node.left
            return
        
        if current_node.key > target_node.key:
            if current_node.left.key == target_node.key:
                if target_node.left == None:
                    current_node.left = target_node.right
                else:
                    current_node.left = target_node.left
            else:
                self._remove_none_or_one_child(current_node.left, target_node)
        else:
            if current_node.right.key == target_node.key:
                if target_node.left == None:
                    current_node.right = target_node.right
                else:
                    current_node.right = target_node.left
            else:
                self._remove_none_or_one_child(current_node.right, target_node)
    
    def __getitem__(self, key):
        return self.find(key)
    
    def __setitem__(self, key, data):
        found_node = self._find_node_rec(key, self.root)

        if found_node.key == key:
            found_node.data = data
        else:
            if found_node.key < key:
                found_node.right = BST_Node(key, data)
            else:
                found_node.left = BST_Node(key, data)

    def __str__(self):
        ret_str = ""

        ret_str += self._print_contents_inorder_rec(self.root)

        return ret_str
    
    def _print_contents_inorder_rec(self, node):
        if node == None:
            return ""
        
        string = ""

        string += self._print_contents_inorder_rec(node.left)

        string += "{" + str(node.key) + ":" + str(node.data) + "}" + " "

        string += self._print_contents_inorder_rec(node.right)

        return string
    
    def __len__(self):
        return self._get_size_rec(self.root)
        
    def _get_size_rec(self, node):
        if node == None:
            return 0
        
        return (self._get_size_rec(node.left) + 1 + self._get_size_rec(node.right))
