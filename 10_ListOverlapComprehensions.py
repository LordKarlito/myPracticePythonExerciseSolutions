"""
Exercise 10 - List Overlap Comprehensions
Level - X X

Take two lists and write a program that returns a list that contains only the elements that are common between the lists. Make sure your program works on two lists of different sizes.

Extra:
- Randomly generate two lists to test this
"""
import random

a = random.sample(range(0, 20), 10)
b = random.sample(range(0, 20), 15)

c = [x for x in a if x in b]

print(a)
print(b)
print(c)