from random import randint

class ItemExistsException(Exception):
    pass

class SLL_Node:
    def __init__(self, key = None, data = None, next = None):
        self.key = key
        self.data = data
        self.next = next
    
class Map_ADT:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_in_map(self, key, node):
        if node == None:
            return False
        elif node.key != key:
            return self.is_in_map(key, node.next)
        else:
            return True
    
    def insert(self, key, value):
        if self.is_in_map(key, self.head):
            raise ItemExistsException()
        else:
            new_node = SLL_Node(key, value, self.head)
            self.head = new_node

            if self.tail == None:
                self.tail = self.head
    
    def find(self, key, node):
        if node == None:
            return node
        elif node.key != key:
            return self.find(key, node.next)
        else:
            return node
    
    def update(self, key, value):
        update_node = self.find(key, self.head)

        if update_node == None:
            self.insert(key, value)
        else:
            update_node.data = value
    
    def remove_rec(self, key, node):
        if node == None:
            return
        elif node.next.key != key:
            self.remove_rec(key, node.next)
        else:
            node.next = node.next.next

    def remove(self, key):
        self.remove_rec(key, self.head)

    def __str__(self):
        ret_str = ""
        current_node = self.head

        while current_node != None:
            ret_str += "{" + str(current_node.key) + ":" + str(current_node.data) + "}" + " "
            current_node = current_node.next

        return ret_str
    
    def get_size_rec(self, node):
        if node == None:
            return 0
        else:
            return 1 + self.get_size_rec(node.next)
    
    def __len__(self):
        return self.get_size_rec(self.head)
    
if __name__ == "__main__":
    m = Map_ADT()

    m.insert(1, "Fuego")
    m.insert(2, "Pyro")
    m.insert(3, "Blizzaga")
    m.insert(4, 99999)

    print(m)
    print(len(m))

    m.update(4, "Thundaga")

    print(m)

    m.remove(1)

    print(m)

    new_lis = []

    for i in range(100):
        new_lis.append(randint(0, 100))
    
    print(new_lis)

    for i in new_lis:
        h = hash(i)
        print(h, end=" ")






        
    
