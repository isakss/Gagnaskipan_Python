"""
This program has a series of simple functions that are examined for
their time complexity using the Big Oh notation.
"""
from random import randint

#The time complexity of programs is dependent on their received input,
#In the case of Abs here below the size of the input doesnt matter however,
#The runtime doesnt get extended by the input, thus the time complexity is constant: O(1)

def abs(value):
    if value < 0:
        return -value
    return value

#The function below iterates through a range of natural numbers and prints them out.
#The loop iterates n times, so we say that the function has a linear time complexity: O(n)

def print_natural_num(n):
    for i in range(1, n + 1):
        print(i)

def big_O1_example():
    counter = 0
    counter += 1
    print(counter)

def big_O_logN_example():
    counter = 0
    n = 10000000000
    i = 1
    while i < n:
        counter += 1
        i *= 2
    print(counter)

def big_O_N_example():
    n = 1000
    counter = 0
    for i in range(n):
        counter += 1
    print(counter)

def big_O_N2_example():
    n = 1000
    counter = 0
    for i in range(n):
        for j in range(n):
            counter += 1
    print(counter)

#The following exercises are implemented to check their time complexity

#This function simply takes in two paramaters and raises the first to the power of the second.
#However, implementing the function without the built in ** operator requires us to make a for loop.
#This raises the time complexity of the function to linear instead of constant.
#Remember: the time complexity is always based on the highest power of n in Big Oh notation
#O(n)

def power(x, y):
    count = 0                                             #O(1)  
    return_value = 1                                      #O(1) 

    if x == 0 and y == 0:                                 #O(1)
        raise Exception("Base and exp cant both be 0")    #O(1)

    for i in range(y):                                    #O(n)  
        return_value *= x                                 #O(1)
        count += 1                                        #O(1)

    print(count)                                             
     
    return return_value

#This function takes in two parameters and multiplies them together without the use of the * operator
#To do that we have to use a for loop that iterates an amount of times equal to the second parameter
#and adds x to a variable that stores the accumulated sum.
#This function thus has a linear time complexity.
#O(n)   
def pos_multiplication(x, y):
    count = 0                     #O(1)
    mult_val = x                  #O(1) 

    for i in range(1,y):          #O(n) 
        mult_val += x             #etc.
        count += 1

    print(count)    
    return mult_val 

#The time complexity of this function is O(n)
#Note: generating a list of size n is an O(n) time complexity operation
def rand_num_insert(n):
    new_list = [0] * n               #O(n), loops n times
    count = 0

    for i in range(n):               #O(n)
        new_list[i] = randint(1,6)
        count += 1

    print(count)
    return new_list

#The time complexity of this function is O(1)
def increment_num_at_index(list_element):
    rand_num = randint(0, len(list_element) - 1) #O(1)
    lis[rand_num] += 1                           #O(1)

def insert_ordered(list_object, value):
    list_object.append(value) #O(1)
    i = len(list_object) - 1  #O(1)

    while True:  #O(n)
        if i == 0: #(O1)
            break
        if list_object[i] > list_object[i-1]: #O(1)
            break
        else:
            temp = list_object[i] #O(1)
            list_object[i] = list_object[i - 1] #O(1)
            list_object[i - 1] = temp #O(1)
            i -= 1 #O(1)



#Function calls go below here

"""
print_natural_num(10)
big_O1_example()
big_O_N_example()
big_O_logN_example()
big_O_N2_example()

print(power(2, 4))
print(pos_multiplication(4, 3))
print(rand_num_insert(10))
"""

lis = []

insert_ordered(lis, 5)
print(lis)
insert_ordered(lis, 7)
print(lis)
insert_ordered(lis, 2)
print(lis)
insert_ordered(lis, 23)
print(lis)
insert_ordered(lis, 78)
print(lis)