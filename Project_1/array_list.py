class IndexOutOfBounds(Exception):
    pass

class Empty(Exception):
    pass

class ArrayList:
    def __init__(self, capacity=20):
        self._capacity = capacity 
        self._size = 0
        self._arr = [0] * self._capacity
     
    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""

        if self._size == 0:
            return return_string
        else:
            for i in range(self._size - 1):
                return_string += str(self._arr[i]) + ", "

            return_string += str(self._arr[self._size - 1])

            return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self._size += 1

        if self._size == self._capacity:
            self.resize()

        for i in range(self._size):
            self._arr[i + 1] = self._arr[i]

        self._arr[0] = value    

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index not in range(self._size):
            raise IndexOutOfBounds()
        else:
            if self._size == self._capacity:
                self.resize()
            
            for i in range(self._size, index, - 1):
                self._arr[i] = self._arr[i - 1]

            self._arr[index] = value
            self._size += 1    


    #Time complexity: O(1) - constant time
    def append(self, value):
        if self._size == self._capacity:
            self.resize()

        self._arr[self._size] = value
        self._size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index not in range(self._size):
            raise IndexOutOfBounds()
        else:
            self._arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self._size == 0:
            raise Empty()
        else:
            return self._arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if index not in range(self._size):
            raise IndexOutOfBounds()
        else:
            return self._arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self._size == 0:
            raise Empty()
        else:
            return self._arr[self._size - 1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        self._capacity *= 2
        new_Arr = ArrayList(self._capacity)

        for i in range(self._size):
            new_Arr._arr[i] = self._arr[i]

        self._arr = new_Arr._arr

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if index not in range(self._size):
            raise IndexOutOfBounds()
        else:
            for i in range(index, self._size -1):
                self._arr[i] = self._arr[i + 1]
            self._size -= 1

    #Time complexity: O(1) - constant time
    def clear(self):
        self._size = 0
        self._arr = [0] * self._capacity

    #Time complexity: O(n) - linear time in size of sublist
    def sublist(self, start, length):
        if (start or length) > self._size or (start or length) < 0:
            raise IndexOutOfBounds()
        else:
            sub_list = ArrayList()

            for i in range(start, start + length):
                sub_list.append(self._arr[i])
            
            return sub_list

    #Time complexity: O(n) - linear time in size of concatinated list
    # OR
    #Time complexity: O(n+m) - linear time in size of both lists, self and other
    def concatenate(self, other):
        concat_list = ArrayList()

        for i in range(self._size):
            concat_list.append(self._arr[i])
        
        for j in range(other._size):
            concat_list.append(other._arr[j])

        return concat_list

if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    """
    arr_lis = ArrayList()
    print(str(arr_lis))
    arr_lis.prepend(5)
    print(str(arr_lis))
    arr_lis.prepend(6)
    print(str(arr_lis))
    arr_lis.append(4)
    print(str(arr_lis))
    print(arr_lis.get_first())
    print(arr_lis.get_last())

    arr_lis.set_at(10, 0)
    print(str(arr_lis))

    arr_lis.insert(12, 2)
    print(str(arr_lis))

    sub_list = arr_lis.sublist(1,3)
    print(str(sub_list))

    arr_lis = arr_lis.concatenate(sub_list)
    print(str(arr_lis))

    arr_lis.remove_at(2)
    print(str(arr_lis))

    arr_lis.clear()
    print(str(arr_lis))

    arr_lis.append(10)
    print(str(arr_lis))
    
    new_arr = ArrayList()

    for i in range(20):
        new_arr.append(i)

    print(str(new_arr))

    new_arr.append(20)

    print(str(new_arr))

    for i in range(20):
        new_arr.append(i)
    """
    

    



    
    