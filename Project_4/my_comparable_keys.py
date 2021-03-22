class MyComparableKey:
    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.str_value = string_value

    def __lt__(self, other):
        if self.int_value < other.int_value:
            return True
        elif self.int_value == other.int_value:
            if self.str_value < other.str_value:
                return True

        return False