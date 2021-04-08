# IMPLEMENT HERE
class TreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        if self.left == None:
            return str(self.data)
        else:
            return str(self.data) + "(" + str(self.left) + "," + str(self.right) + ")"

class BooleanTree:
    def __init__(self):
        self.root = None
    
    def __str__(self):
        return str(self.root)
    
    def build_tree_rec(self, char_list):
        char = char_list.pop()
        ret_node = TreeNode(char)
        if char == "AND" or char == "OR":
            ret_node.left = self.build_tree_rec(char_list)
            ret_node.right = self.build_tree_rec(char_list)
        elif char == "T":
            ret_node.data = True
        elif char == "F":
            ret_node.data = False
        return ret_node

    def build_tree(self, statement_string):
        clean_statement_string = statement_string.replace("(", " ").replace(")", " ").replace(",", " ").split()
        clean_statement_string.reverse()
        self.root = self.build_tree_rec(clean_statement_string)
    
    def get_root_value_rec(self, node):
        if node.left == None:
            return node.data
        else:
            if node.data == "AND":
                return self.get_root_value_rec(node.left) and self.get_root_value_rec(node.right)
            elif node.data == "OR":
                return self.get_root_value_rec(node.left) or self.get_root_value_rec(node.right)
            
    def get_root_value(self):
        return self.get_root_value_rec(self.root)

if __name__ == "__main__":

    print("\nSHOWING HOW TO LOSE THE DELIMITERS, IF WANTED")
    statement_string = "OR(AND(T,F),F)"
    print(statement_string)
    # YOU CAN DO THIS IN YOUR build_tree() OPERATION IF THE LIST FORMAT FEELS BETTER
    statement_list = statement_string.replace("(", " ").replace(")", " ").replace(",", " ").split()
    print(statement_list)


    print("\n\nTESTING BOOLEAN TREE\n")

    # THESE TESTS SHOULD WORK EXACTLY AS THEY ARE BUT FEEL FREE TO MAKE MORE EXTENSIVE TESTS AS WELL

    bt = BooleanTree()
    statement_string = "OR(AND(T,F),F)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "OR(T,AND(T,F))"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "OR(AND(T,T),F)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(T,OR(F,F))"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(OR(F,T),T)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(F,F)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(OR(OR(F,F),T),OR(T,AND(T,F)))"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())