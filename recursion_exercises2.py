"""
This program is a collection of recursion exercises implemented on lists and similar structures
"""

# Exercise 1: Recursive function that finds the length of a string

def str_len_rec(string_object):
    if string_object == "":
        return 0
    else:
        return 1 + str_len_rec(string_object[1:])

print(str_len_rec("wizard"))

# Exercise 2: Recursive function for linear search of a value n within a list

def lin_srch_rec(list_object, target_val):
    if list_object == []:
        return False
    elif list_object[0] == target_val:
        return True 
    else:
        return lin_srch_rec(list_object[1:], target_val)

print(lin_srch_rec([1,2,4,4,5,8,9,10], 1))

# Exercise 3: Recursive function to count instances of element n within a list

def count_occ_rec(list_object, value):
    if list_object == []:
        return 0
    elif list_object[0] == value:
        return 1 + count_occ_rec(list_object[1:], value)
    else:
        return 0 + count_occ_rec(list_object[1:], value)

print(count_occ_rec([1,2,3,2,5,6,7,8,2], 2))

# Exercise 4: Recursive function that removes duplicates from a list

def rem_dup_rec(list_object):
    if list_object == []:
        return []
    elif lin_srch_rec(list_object[1:], list_object[0]):
        return [] + rem_dup_rec(list_object[1:])
    else:
        return [list_object[0]] + rem_dup_rec(list_object[1:])

print(rem_dup_rec([2,2,2,3,3,3,4,4,4,5,5,5]))

# Exercise 5: Binary Search on ordered list with recursive programming

def bin_srch_rec(list_object, target_val, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target_val == list_object[mid]:
            return True
        elif target_val < list_object[mid]:
            return bin_srch_rec(list_object, target_val, low, mid - 1)
        else:
            return bin_srch_rec(list_object, target_val, mid + 1, high)

print(bin_srch_rec([1, 3, 4, 25, 66, 109, 205], 33, 0, 7))

# Exercise 6: susbtring finder, returns true if a given string is a substring of a second string

def is_prefix(prefix, a_str):
    if len(prefix) == 0:
        return True
    elif len(a_str) == 0:
        return False
    if prefix[0] != a_str[0]:
        return False
    else:
        return is_prefix(prefix[1:], a_str[1:])    

def is_substring(substring, a_str):
    if len(a_str) == 0:
        if len(substring) == 0:
            return True
        else:
            return False
    if is_prefix(substring, a_str):
        return True
    return is_substring(substring, a_str[1:])

print(is_substring("naski", "gagnaskipan"))

# Exercise 7: Recursive functions elf-ish and x-ish, that determine whether a string includes all the letters in a substring

def is_in_string(a_string, char):
    if len(a_string) == 0:
        return False
    if a_string[0] == char:
        return True
    else:
        return is_in_string(a_string[1:], char)

def xish(x_string, a_string):
    if len(x_string) == 0:
        return True
    elif is_in_string(a_string, x_string[0]):        
        return xish(x_string[1:], a_string)
    return False

print(xish("a", "gagnaskipan"))
print(xish("gski", "gagnaskipan"))

# Exercise 8: Create the function is_palindrome, which recursively checks a string to see whether the string is a palindrome

def is_palindrome(a_string, reverse_string):
    if len(a_string) == 0:
        return True
    if a_string[0] != reverse_string[-1]:
        return False
    else:
        return is_palindrome(a_string[1:], reverse_string[:-1])

print(is_palindrome("rumur", "rumur"))

    


