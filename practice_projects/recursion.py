# A collection of recursive projects

# Problem 1.1

def fac(n):
    if n <= 0:
        return 1
    else:
        return n * fac(n - 1)

# Problem 1.2

def my_pow(a, b):
    if b <= 0:
        return 1
    else:
        return a * my_pow(a, b - 1)

# Problem 1.3

def my_int(string):
    if len(string) == 1:
        return ord(string[0]) - ord("0")

    y = my_int(string[1:])
    x = ord(string[0]) - ord("0")
    x = x * (10**(len(string) - 1)) + y
    return int(x)


# Problem 1.4

def fib(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fib(n - 1)
        return (a + b, a)

# Problem 1.5

def print_range(a, b):
    if a > b:
        return
    else:
        print(a, end=" ")
        print_range(a + 1, b)

# Problem 1.6

def binary_strings(n):
    if n == 0:
        return [""]
    
    smaller = binary_strings(n - 1)

    begins_with_one = ["1" + x for x in smaller]
    begins_with_zero = ["0" + x for x in smaller]

    return begins_with_one + begins_with_zero

# Problem 1.7

def _get_subsets_rec(list_object, i):
    if i == len(list_object):
        return [[]]
    
    smaller = _get_subsets_rec(list_object, i + 1)

    with_element_i = [[list_object[i]] + element for element in smaller]

    return smaller + with_element_i

def subset(st):
    return _get_subsets_rec(st, 0)

# Problem 1.8

def permutations(lis):
    if lis == []:
        return [[]]
    
    ret_lis = []

    for i in range(len(lis)):
        sub_lis = lis[:i] + lis[i+1:]

        for perm in permutations(sub_lis):
            ret_lis.append([lis[i]] + perm)
        
    return ret_lis


if __name__ == "__main__":
    print(fac(10))
    print(my_pow(2,3))
    print(my_int("456789"))
    print(fib(10))
    print(print_range(1, 10))
    print(binary_strings(3))
    print(subset([1, 2, 3]))
    print(permutations([1, 2, 3]))