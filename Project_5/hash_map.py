class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Bucket_Node:
    def __init__(self, key = None, data = None, next = None):
        self.key = key
        self.data = data
        self.next = next

class Bucket:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert(self, key, data):
        if not self.contains(key):
            new_node = Bucket_Node(key, data, self.head)
            self.head = new_node

            if self.tail == None:
                self.tail = self.head
            
            self.size += 1
        else:
            raise ItemExistsException()
    
    def update(self, key, data):
        node = self.find_rec(key, self.head)

        if node == None:
            raise NotFoundException()
        else:
            node.data = data

    def find_rec(self, key, node):
        if node == None:
            return None
        elif node.key == key:
            return node
        else:
            return self.find_rec(key, node.next)

    def find(self, key):
        node = self.find_rec(key, self.head)

        if node == None:
            raise NotFoundException()
        else:
            return node.data
    
    def contains(self, key):
        if self.find_rec(key, self.head) != None:
            return True
        else:
            return False
    
    def find_prev_node_rec(self, key, node):
        if node.key == key:
            return node
        elif node.next == None:
            return None
        elif node.next.key == key:
            return node
        else:
            return self.find_prev_node_rec(key, node.next)

    def remove(self, key):
        node = self.find_prev_node_rec(key, self.head)

        if node == self.head and node.key == key:
            self.head = self.head.next    
        elif node == None:
            raise NotFoundException()
        else:
            node.next = node.next.next
        
        self.size -= 1
    
    def __getitem__(self, key):
        return self.find(key)
    
    def __setitem__(self, key, data):
        if self.contains(key):
            return self.update(key, data)
        else:
            self.insert(key, data)
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        self._it = Bucket_Node(None, None, self.head)
        return self
    
    def __next__(self):
        if self._it.next == None:
            raise StopIteration()
        else:
            self._it = self._it.next
            return self._it

    """
    def __str__(self):
        current_node = self.head
        ret_str = ""

        while current_node != None:
            ret_str += "{" + str(current_node.key) + ":" + str(current_node.data) + "}" + " "
            current_node = current_node.next
         
        return ret_str
    """

class HashMap:
    def __init__(self, capacity = 4, size = 0):
        self._bucket_list = [Bucket() for _ in range(capacity)]
        self._capacity = capacity
        self._size = size
    
    def _hashing_function(self, key):
        return (hash(key) % self._capacity)

    def insert(self, key, data):
        h = self._hashing_function(key)
        self._bucket_list[h].insert(key, data)
        self._size += 1

        if self._size >= (1.20 * self._capacity):
            self.rebuild()

    def update(self, key, data):
        h = self._hashing_function(key)
        self._bucket_list[h].update(key, data)
    
    def find(self, key):
        h = self._hashing_function(key)
        return self._bucket_list[h].find(key)
    
    def contains(self, key):
        h = self._hashing_function(key)
        return self._bucket_list[h].contains(key) 

    def remove(self, key):
        h = self._hashing_function(key)
        self._bucket_list[h].remove(key)
        self._size -= 1

    def rebuild(self):
        self._capacity *= 2
        new_bucket_list = HashMap(self._capacity)

        for i in self._bucket_list:
            for j in i:
                new_bucket_list.insert(j.key, j.data)
        
        self._bucket_list = new_bucket_list._bucket_list
    
    def __setitem__(self, key, data):
        if self.contains(key):
            return self.update(key, data)
        else:
            self.insert(key, data)
    
    def __getitem__(self, key):
        return self.find(key)
    
    def __len__(self):
        return self._size
    
    """
    def __str__(self):
        ret_lis = []

        for i in self._bucket_list:
            amount = 0
            for j in i:
                amount += 1
            ret_lis.append(amount)
        
        return str(ret_lis)
    """

"""
if __name__ == "__main__":
    hm = HashMap()

    
    hm.insert(1, 50)
    hm.insert(23, "Flare")
    hm.insert(5, 55)
    hm.insert(6, "Thundaga")
    hm.insert(7, "Thundaga")
    hm.insert(8, "Thundaga")
    hm.insert(9, "Thundaga")

    hm.insert(600, "Thundaga")
    hm.insert(60000, "Flare")

    for i in range(64):
        hm.insert(randint(1, 10000000), 565656)

    print(hm)
    print(hm._capacity)
    # TODO: test everything but insert and print

    print(hm.contains(60000))
    print(hm.find(60000))

    hm.update(600, "Xenoglossy")
    print(hm.find(600))

    print(hm[60000])
    hm[60000] = "Firaga"

    print(hm[60000])

    print(len(hm))

    hm.remove(600)

    print(len(hm))

    print(hm[600])

    
    
    print(len(hm))

    print(hm[23])

    hm[23] = "Xenoglossy"

    print(hm)

    print(hm.contains(23))

    for i in hm:
        print(i)

    hm.insert(36, "Dispair")

    for i in hm:
        print(i)

    hm.remove(23)
    hm.remove(1)
    hm.remove(5)

    print(hm)

    print(len(hm))
"""





        