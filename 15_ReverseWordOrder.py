"""
Exercise 15: Reverse Word Order
Level: X X X

Write a program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.

Example: My name is Michelle => Michelle is name My
"""

myString = input("Enter a sentence: ")

def splitter(myString):
    newString = myString.split()
    reversedString = newString[::-1]
    return(" ".join(reversedString))

print(splitter(myString))