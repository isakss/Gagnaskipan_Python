from my_hashable_key import *
from random import *

# READ THIS!!
# DO NOT USE THE BUILT-IN HASH
# FUNCTIONS FOR INTEGERS AND STRINGS!
# MAKE SURE YOUR IMPLEMENTATION OF
# __hash__ RETURNS A POSITIVE INTEGER!

if __name__ == "__main__":
    k1 = MyHashableKey(1, "one")
    print(hash(k1))
    k2a = MyHashableKey(2, "two")
    print(hash(k2a))
    k2b = MyHashableKey(2, "two")
    print(hash(k2b))
    print(k1 == k2a)
    print(k2a == k2b)

    capacity = 20
    new_lis = [0] * 20
    
    for i in range(100):
        position = MyHashableKey(randint(1, 1000000), "Flippo")

        new_lis[hash(position) % capacity] += 1
    
    print(new_lis)

