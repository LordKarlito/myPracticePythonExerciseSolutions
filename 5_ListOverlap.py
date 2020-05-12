"""
Exercise 5 - List Overlap
Level - X X

Take two lists and write a program that returns a list that contains only the elements that are common between the lists. Make sure your program works on two lists of different sizes.

Extras:
1. Randomly generate two lists to test this
2. Write this in one line of Python
"""

import random

a = random.sample(range(0,20), 10)
b = random.sample(range(0,20), 15)

c = [x for x in a if x in b]

print(a)
print(b)
print(c)

def setFunction(a,b):
    c = set()

    for x in b:
        if x in a:
            c.add(x)
    # c.add(x for x in a if x in b)

    return(list(c))

print(setFunction(a,b))