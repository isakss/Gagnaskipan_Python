class MyHashableKey:
    def __init__(self, int_value = 0, string_value = ""):
        self.int_value = int_value
        self.string_value = string_value
    
    def __eq__(self, other):
        if self.int_value == other.int_value and self.string_value == other.string_value:
            return True
        else:
            return False
    
    def __hash__(self):
        res_val = 0

        for i, char in enumerate(self.string_value):
            res_val += (ord(char)**i) * self.int_value
        
        return res_val
            
