"""
A program consisting of multiple test functions to test the Stopwatch class
"""

from Stopwatch import Stopwatch
import random

def get_from_list_test():
    n = 100000
    new_list = [i for i in range(n)]

    timer = Stopwatch()
    timer.StartTime()

    for i in range(10000):
        x = new_list[random.randint(0, n - 1)]
    
    timer.StopTime()
    timer.GetTime()

def find_in_list_test():
    a = 0
    n = 100000
    new_list = [random.randint(0, 3 * n) for i in range(n)]

    timer = Stopwatch()
    timer.StartTime()

    for i in range(10000):
        if random.randint(0, n*3) in new_list:
            a = a + 1
    
    timer.StopTime()
    timer.GetTime()

def find_in_dictionary_test():
    a = 0
    new_dict = {}
    n = 100000
    
    for i in range(n):
        num = random.randint(0,n*3)
        new_dict[num] = num

    timer = Stopwatch()
    timer.StartTime()

    for i in range(10000):
        if random.randint(0, n*3) in new_dict:
            a = a + 1
    
    timer.StopTime()
    timer.GetTime()

def test_list_prepend():
    n = 100000
    new_list = []

    timer = Stopwatch()
    timer.StartTime()

    for i in range(n):
        new_list.insert(0,random.randint(0, n*3))
        
    timer.StopTime()
    timer.GetTime()

def test_list_append():
    n = 100000
    new_list = []
    
    timer = Stopwatch()
    timer.StartTime()

    for i in range(n):
        new_list.append(random.randint(0, n*3))
        
    timer.StopTime()
    timer.GetTime()

def main():
    get_from_list_test()
    find_in_list_test()
    find_in_dictionary_test()
    test_list_append()
    test_list_prepend()

main()