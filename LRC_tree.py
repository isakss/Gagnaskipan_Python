class LRC_Node:
    def __init__(self, left = None, right = None, center = None, data = None):
        self.left = left
        self.right = right
        self.center = center
        self.data = data

class LRCMap:
    def __init__(self, build = False):
        self.root = None
        if build:
            self.root = self._build(8)
        else:
            self.root = LRC_Node()
    
    def _build(self, levels):
        if levels < 0:
            return None
        
        node = LRC_Node()
        node.left = self._build(levels - 1)
        node.right = self._build(levels - 1)
        node.center = self._build(levels - 1)

        return node
    
    def _put_data_rec(self, node, key, data):
        if node == None:
            node = LRC_Node()
        if key == "":
            node.data = data
        elif key[0] == "l":
            node.left = self._put_data_rec(node.left, key[1:], data)
        elif key[0] == "r":
            node.right = self._put_data_rec(node.right, key[1:], data)
        elif key[0] == "c":
            node.center = self._put_data_rec(node.center, key[1:], data)
        return node
    
    def put_data(self, key, data):
        self._put_data_rec(self.root, key, data)
    
    def _get_data_recur(self, node, key):
        if node == None:
            return None
        if key == "":
            return node.data
        elif key[0] == "l":
            return self._get_data_recur(node.left, key[1:])
        elif key[0] == "r":
            return self._get_data_recur(node.right, key[1:])
        elif key[0] == "c":
            return self._get_data_recur(node.center, key[1:])
    
    def get_data(self, key):
        return self._get_data_recur(self.root, key)


if __name__ == "__main__":    
    # MAKE ALL TEST CODE BELOW THIS LINE    
    # # AND AT THIS INDENT LEVEL!!    
    tm = LRCMap()    
    tm.put_data("lrl", "THIS IS THE DATA FOR KEY lrl")    
    tm.put_data("lc", "THIS IS THE DATA FOR KEY lc")    
    print(tm.get_data("lrl"))    
    print(tm.get_data("lrcclc"))    
    print(tm.get_data("lc"))    
    tm = LRCMap(True)    
    tm.put_data("lrlrccr", "THIS IS THE DATA FOR KEY lrlrccr")    
    tm.put_data("lrlrcclc", "THIS IS THE DATA FOR KEY lrlrcclc")    
    print(tm.get_data("lrlrcclc"))    
    print(tm.get_data("lrlclc"))    
    print(tm.get_data("lrlrccr"))