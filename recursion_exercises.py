""" This program contains a series of recursive functions as practice """

# Teacher examples:

def my_example():           # Default function would look something like this
    print("second")
    my_example2()

def my_example2():          # Normally a function with no return statements returns a None type 
    print("third")


print("first")              # Normally when we call functions their function calls enter a stack of sorts based on which function call occured last
my_example()
print("last")

def my_recursive_example(n):      # Here we define a recursive function which calls itself instead of making use of iterator loops
    print(n)                      # Recursive functions have to have some kind of base case to move towards that will result in the end of the recursion
    if n <= 0:                    # Otherwise recursive functions call themselves with different parameters based on some operations
        return
    else:
        my_recursive_example(n - 1)

my_recursive_example(100)

# Practice Exercises

# pow function

def power_recursive(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power_recursive(base, (exp - 1))

print(power_recursive(2,8))

# Multiplication with + and -

def multip_recursive(a, b):
    if b == 0:
        return 0
    elif b > 0:
        if b == 1:
            return a
        else:
            return a + multip_recursive(a, b - 1)
    else:
        if b == 1:
            return a
        else:
            return - (a - multip_recursive(a, b + 1))

print(multip_recursive(2, 10))
print(multip_recursive(2, -10))
print(multip_recursive(1, 2))
print(multip_recursive(1, -1))
print(multip_recursive(-2, -10))

# Factorial function

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(factorial_recursive(5))

# First n natural numbers

def print_natural(n):
    if n > 0:
        print_natural(n - 1)
        print(n, end=" ")                #Printing the values after the function calls will result in them being printed in reversed order after every call has been resolved

print_natural(5)
print()

# print the sum of a parameters digits by recursion

def sum_of_digits_recursive(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits_recursive(n//10)

print(sum_of_digits_recursive(254)) 

# Fibonacci sequence using recursion, note that the upper function has a time complexity of O(n2) while the lower has a time complexity of O(n)

def bad_fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci_recursive(n - 2) + bad_fibonacci_recursive(n - 1)

def good_fibonacci_recursive(n):
    if n <= 1:
        return (n, 0)
    else: 
        (a, b) = good_fibonacci_recursive(n - 1)                    # Having only a single recursion call makes this function more time efficient than the other
        return (a + b, a)

print(good_fibonacci_recursive(10))
print(bad_fibonacci_recursive(10))