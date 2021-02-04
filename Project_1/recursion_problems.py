
def less_than(a, b):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    if a == 0:
        return True
    if b == 0:
        return False
    if a == b:
        return False
    else:
        return less_than(a - 1, b - 1)

def unique(lis1):
    current_element = lis1[0]

    if len(lis1) == 1:
        return lis1
    elif current_element in lis1[1:]:
        return unique(lis1[1:])
    else:
        return [current_element] + unique(lis1[1:])

# FEEL FREE TO EDIT THE TESTS AND MAKE THEM BETTER
# REMEMBER EDGE CASES!

def test_less_than(num1, num2):
    if(less_than(num1, num2)):
        print(str(num1) + " is less than " + str(num2))
    else:
        print(str(num1) + " is NOT less than " + str(num2))

def test_unique(lis1):
    print(str(unique(lis1)) + " are the unique items in " + str(lis1))

def run_recursion_program():

    print("\nTESTING LESS THAN:\n")

    test_less_than(8, 3)
    test_less_than(2, 9)
    test_less_than(4, 17)
    test_less_than(11, 3)
    test_less_than(8, 2)
    test_less_than(8, 7)
    test_less_than(7, 8)
    test_less_than(6, 16)
    test_less_than(7, 7)

    print("\nTESTING UNIQUE:\n")

    test_unique(['a', 'f', 'd', 't', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['a', 'b', 'f', 'g', 'a', 't', 'c', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['f', 'g', 't', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'])
    test_unique(['t'])


if __name__ == "__main__":
    run_recursion_program()