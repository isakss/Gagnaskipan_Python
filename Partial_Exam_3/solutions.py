class HashTable:
    def __init__(self):
        #set a fixed  capacity
        self.capacity = 16
        #create the bucketlist
        self.bucket_list = []

        #fill the bucketlist with empty arrays
        for i in range(self.capacity):
            self.bucket_list.append([])
    
    def _hashing_function(self, key):
        return (hash(key) % self.capacity)

    def insert(self, key):
        h = self._hashing_function(key)

        if key in self.bucket_list[h]:
            pass
        else:
            self.bucket_list[h].append(key)

    def contains(self, key):
        h = self._hashing_function(key)

        if key in self.bucket_list[h]:
            return True
        else:
            return False

    def remove(self, key):
        h = self._hashing_function(key)

        if key in self.bucket_list[h]:
            self.bucket_list[h].remove(key)
        else:
            pass

class PrefixParsingTreeNode:
    def __init__(self, token, left, right):
        self.token = token
        self.left = left
        self.right = right

class PrefixParsingTree:
    def __init__(self):
        self.root = None

    class Tokenizer:
        def __init__(self, str_statement):
            self.statement = str_statement
            self.position = 0

        def get_next_token(self):
            i = self.position
            while i < len(self.statement) and self.statement[i] != " ":
                i += 1
            ret_val = self.statement[self.position:i]
            self.position = i + 1
            return ret_val

    def build_tree_recursive(self, tokenizer):
        token = tokenizer.get_next_token()

        if token == "+" or token == "-":
            return PrefixParsingTreeNode(token, self.build_tree_recursive(tokenizer), self.build_tree_recursive(tokenizer))
        elif token.isdigit():
            return PrefixParsingTreeNode(token, None, None)
        else:
            return PrefixParsingTreeNode(token, None, None)

    def load_statement_string(self, statement):
        tokenizer = self.Tokenizer(statement)
        self.root = self.build_tree_recursive(tokenizer)

    def preorder_calculation_rec(self, node):
        if node.token == "+":
            return (self.preorder_calculation_rec(node.left) + self.preorder_calculation_rec(node.right))
        elif node.token == "-":
            return (self.preorder_calculation_rec(node.left) - self.preorder_calculation_rec(node.right))
        else:
            return int(node.token)

    def calculate_value(self):
        return self.preorder_calculation_rec(self.root)

class FileTreeNode:
    def __init__(self):
        self.string = None
        self.children = []

def parser_bracket_string_rec(current_node, bracket_str, str_index):
    current_bullet_string = ""

    while True:
        if bracket_str[str_index] == "{":
            next_node = FileTreeNode()
            current_node.children.append(next_node)
            str_index = parser_bracket_string_rec(next_node, bracket_str, str_index + 1)
        elif bracket_str[str_index] == "}":
            current_node.string = current_bullet_string
            return str_index + 1
        else:
            current_bullet_string += bracket_str[str_index]
            str_index += 1

def parse_bracket_file(filename):
    # IMPLEMENT THIS OPERATION
    # YOU CAN IMPLEMENT ONE OR MORE CLASSES
    # YOU CAN MAKE HELPER FUNCTIONS AS NEEDED
    input_file = open(filename)
    bracket_str = input_file.readline()
    i = 0

    while bracket_str[i] != "{":
        i += 1
    
    root = FileTreeNode()
    parser_bracket_string_rec(root, bracket_str, i+1)

    return root

def write_bullets_rec(file_object, node, level):
    for child in node.children:
        for _ in range(level):
            file_object.write("\t")
        file_object.write(child.string + "\n")
        write_bullets_rec(file_object, child, level + 1)

def write_bulleted_file(filename, my_tree):
    # IMPLEMENT THIS OPERATION
    # YOU CAN IMPLEMENT ONE OR MORE CLASSES
    # YOU CAN MAKE HELPER FUNCTIONS AS NEEDED
    output_file = open(filename, "w")
    write_bullets_rec(output_file, my_tree, 1)

def write_labelled_file_rec(file_object, node, level):
    for i in range(len(node.children)):
        child = node.children[i]

        for _ in range(level):
            file_object.write("\t")
        
        if level == 0:
            file_object.write(str(i + 1) + ".\t")
        elif level == 1:
            file_object.write(chr(ord("a") + i) + ")\t")
        else:
            file_object.write("-\t")

        file_object.write(child.string + "\n")
        write_labelled_file_rec(file_object, child, level + 1)


def write_labelled_file(filename, my_tree):
    # IMPLEMENT THIS OPERATION
    # YOU CAN IMPLEMENT ONE OR MORE CLASSES
    # YOU CAN MAKE HELPER FUNCTIONS AS NEEDED
    output_file = open(filename, "w")
    write_labelled_file_rec(output_file, my_tree, 0)

def test_hash_table():
    t = HashTable()
    t.insert("test1")
    t.insert("test2")
    t.insert("test3")
    t.insert("test1")
    print(t.contains("test3"))
    print(t.contains("test1"))
    print(t.contains("test4"))
    t.remove("test3")
    print(t.contains("test3"))
    t.remove("test1")
    print(t.contains("test2"))
    print(t.contains("test1"))

# OPERATION FOR TESTING THE PREFIX PARSING TREE
# DONT CHANGE
def test_prefix_tree(statement_string):
    print("This is the statement: " + statement_string)
    ppt = PrefixParsingTree()
    ppt.load_statement_string(statement_string)
    print("This is the result: " + str(ppt.calculate_value()))

# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!
    print("testing hash table")
    test_hash_table()
    
    print("testing prefix tree")
    test_prefix_tree("- 12 + 4 5")
    test_prefix_tree("+ 12 + - 21 5 5")
    test_prefix_tree("+ 4 + - 4 6 - 9 8")
    test_prefix_tree("- + - + 6 9 8 + 1 + 5 5 - - + 6 7 - 9 8 - + 9 6 1")
    test_prefix_tree("+ + 8 4 - + - 3 3 2 - + 7 8 9")

    bullet_list_tree = parse_bracket_file("bracket_file_01.txt")
    write_bulleted_file("bullet_file_01.txt", bullet_list_tree)
    write_labelled_file("label_file_01.txt", bullet_list_tree)
