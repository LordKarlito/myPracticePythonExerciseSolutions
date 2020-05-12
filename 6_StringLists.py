"""
Exercise 6 - String Lists
Level - X X

Ask the user for a string and print out whether this string is a palindrome or not.
"""

string = input("Enter a word: ")

if string == string[-1:-(len(string)+1):-1]:
    print("{} is a palindrome!".format(string))
else:
    print("{} is NOT a palindrome!! \nThe reverse form the word is {}".format(string, string[-1:-(len(string)+1):-1]))
