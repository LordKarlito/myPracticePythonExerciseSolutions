"""
Exercise 12 - List Ends
Level - X

Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list. 

Extra:
- Write this code inside a function.
"""

myList = [5, 10, 15, 20, 25]

def makeList(myList):
    return([x for x in myList if (x == myList[0] or x == myList[-1])])

print(makeList(myList))