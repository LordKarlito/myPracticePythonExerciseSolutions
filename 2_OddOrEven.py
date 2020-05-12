"""
Exercise 2 - Odd Or
Level - X
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check and one number to divide by. if the divisor divides evenly into dividend, tell that to the user. If not, print a different appropriate message.
"""

number = int(input("Enter a number: "))

if (number % 2 != 0):
    message = "{} is an odd number!".format(number)
else:
    message = "{} is an even number!".format(number)
print(message)