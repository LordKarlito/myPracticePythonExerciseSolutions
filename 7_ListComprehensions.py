"""
Exercise 7 - List Comprehensions
Level - X X

Write one line of python that takes a list and makes a new list that only has the even elements of the list in it
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [x for x in a if x % 2 == 0]

print(b)
