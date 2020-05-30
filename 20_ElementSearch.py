"""
Exercise 20: Element Search
Level: X

Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:
- Use binary search
"""

import random

def binarySearch(arr, num):
    print(arr)
    size = len(arr)
    print(size)
    element = arr[0]
    isFound = False
    if size > 1:
        while isFound == False:
            element = arr[int(size/2)]

            # if size == 0:
            #     isFound = False
            #     break

            print("Evaluate: {} and {}".format(num,element))
            if num == element:
                isFound = True
                print("BREAK")
                break

            elif num < element:
                arr = arr[:int(size/2)]
                binarySearch(arr, num)
                break

            elif num > element:
                arr = arr[int(size/2)+1:]
                binarySearch(arr, num)
                break

        # isFound = True      

    if size == 1 and num == arr[0]:
        isFound = True

    return isFound

arr = random.sample(range(0, 20), 15)
arr.sort()
# arr = [1, 3, 5, 30, 42, 43, 500]
num = int(input("Enter number to search: "))

print(binarySearch(arr, num))